from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Listing, Bid, Watchlist, ListingComments
from django.db import models
from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required


# items for the form, inherits from forms
class NewListingForm(forms.Form):
    title = forms.CharField(label="TITLE", max_length=24,
                error_messages={
                    'required': 'Your listing needs a title',
                    'max_length': 'The title is too long.',
                    })

    content = forms.CharField(label="CONTENT",
                min_length=1024,
                widget=forms.Textarea(attrs={'rows': 20}),
                error_messages={
                    'required': 'Your product description needs at least 40 characters.',
                    'min_length': 'The text is too short, a product description needs at least 40 characters.',
                    })

    # hidden input 'edit' to check if it is a new page, or a editing page
    is_edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)


def index(request):

    # Custom SQL query to fetch the latest bidding_value for each Listing
    query = """
    SELECT
        auctions_listing.*,
        bids.bidding_value AS latest_bidding_value
    FROM
        auctions_listing
    LEFT JOIN (
        SELECT
            product_id,
            bidding_value
        FROM
            auctions_bid
        WHERE
            (product_id, date_bidding) IN (
                SELECT
                    product_id,
                    MAX(date_bidding) AS max_date_bidding
                FROM
                    auctions_bid
                GROUP BY
                    product_id
            )
    ) AS bids ON auctions_listing.id_product = bids.product_id
    WHERE auctions_listing.status = 'ACT' OR auctions_listing.status = 'SOL'
    ORDER BY
        auctions_listing.date_added DESC
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        listing_products = cursor.fetchall()

    # Extract the field names from the cursor description
    columns = [desc[0] for desc in cursor.description]

    # Convert the result into a list of dictionaries
    listing_products = [dict(zip(columns, row)) for row in listing_products]

    return render(request, "auctions/index.html", {
        "listing_products": listing_products,
        "categories": Listing.ListingCategory
    })

def active(request):
        # Custom SQL query to fetch the latest bidding_value for each Listing
    query = """
    SELECT
        auctions_listing.*,
        bids.bidding_value AS latest_bidding_value
    FROM
        auctions_listing
    LEFT JOIN (
        SELECT
            product_id,
            bidding_value
        FROM
            auctions_bid
        WHERE
            (product_id, date_bidding) IN (
                SELECT
                    product_id,
                    MAX(date_bidding) AS max_date_bidding
                FROM
                    auctions_bid
                GROUP BY
                    product_id
            )
    ) AS bids ON auctions_listing.id_product = bids.product_id
    WHERE auctions_listing.status = 'ACT'
    ORDER BY
        auctions_listing.date_added DESC
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        listing_products = cursor.fetchall()

    # Extract the field names from the cursor description
    columns = [desc[0] for desc in cursor.description]

    # Convert the result into a list of dictionaries
    listing_products = [dict(zip(columns, row)) for row in listing_products]

    return render(request, "auctions/index.html", {
        "listing_products": listing_products,
        "categories": Listing.ListingCategory
    })

def select_category(request):
    if request.method == "POST":
        category = request.POST["product_category"]
        if not category == "No_cat": #if user didn't select a category
            listing_products = Listing.objects.filter(category=category, status="ACT" )
        else:
            listing_products = Listing.objects.filter(status="ACT")

    return render(request, "auctions/index.html", {
        "listing_products": listing_products,
        "categories": Listing.ListingCategory
    })

def login_view(request, next=None):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if next:
                return redirect(next)
            else:
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def product(request, id_product, error_bidding=""):
    product_details = Listing.objects.get(id_product=id_product)
    owns_product = False
    wishlisted = False
    #comments_product = ListingComments.objects.get(product=product_details)

    all_bids = Bid.objects.filter(product=product_details)

    try:
        highest_bidding = max(all_bids, key=lambda bid: bid.bidding_value)
        high_bidding = highest_bidding.bidding_value
        high_bidder = highest_bidding.bidder
    except ValueError: #if there are no bids yet
        high_bidding = None
        high_bidder = None


    try:
        # check if product is sold and bought by authenticated user
        if product_details.status == "SOL" and high_bidder == request.user:
            sold_to_user = True
        else:
            sold_to_user = False


        # check if product is watchlisted by authenticated user
        if product_details.seller == request.user: # user can't wishlist own product
            owns_product = True
        else:
            try:
                w = Watchlist.objects.get(product = product_details, buyer = request.user)
                wishlisted = True
            except Watchlist.DoesNotExist:
                wishlisted = False


        # check if authenticated user is the high bidder
        if not high_bidder == None and high_bidder == request.user:
            winning_bidding = "Congratulations, you are winning this bid war!"
        else:
            winning_bidding= ""

        return render(request, "auctions/product.html", {
                "product": product_details,
                "wishlisted": wishlisted,
                "owns_product": owns_product,
                "max_bidding": high_bidding,
                "error_bidding": error_bidding,
                "winning_bidding": winning_bidding,
                "sold_to_user": sold_to_user
            })

    except (TypeError, ValueError):

        return HttpResponseRedirect(reverse("login"))


def new_listing(request):

    if request.method == "GET":
        return render(request,"auctions/new_listing.html", {
            "categories": Listing.ListingCategory,
            "status": Listing.ListingStatus
        })
    else:
        # get data from form
        title = request.POST["title"]
        description = request.POST["description"]
        min_bidding = request.POST["min_bidding"]
        closing_date = request.POST["closing_date"]
        product_category = request.POST["product_category"]
        product_status = request.POST["product_status"]
        photo_url = request.POST["photo"]

        # create a new product
        product_listing = Listing(title=title, description=description, min_bidding= min_bidding,
                                    seller= request.user, date_end_bidding=closing_date, status =product_status,
                                    category= product_category, photo_url=photo_url  )
        # save product
        product_listing.save()

        return HttpResponseRedirect(reverse("product", kwargs={"id_product": product_listing.id_product}))


def add_watchlist(request, id_product):
    if request.method == "POST":
        product = Listing.objects.get(id_product=id_product) # create a product based on product_id
        w = Watchlist(product = product, buyer = request.user) #create a watchlist item
        w.save() # save watchlist


        return HttpResponseRedirect(reverse("product", kwargs={"id_product": id_product}))

def remove_watchlist(request, id_product):
    if request.method == "POST":
        product = Listing.objects.get(id_product=id_product) # create a product based on product_id

        try:
            w = Watchlist.objects.get(product = product, buyer = request.user)
            w.delete() # delete item from watchlist
            wishlisted = False # means user can add item to wishlist again
        except Watchlist.DoesNotExist:
            pass #does nothing

        return HttpResponseRedirect(reverse("product", kwargs={"id_product": id_product}))

def wishlist(request):
    return render(request, "auctions/wishlist.html", {
        "watchlist": Watchlist.objects.filter(buyer = request.user)
    })

def bidding(request, id_product):
    if request.method == "POST":
        product_details = Listing.objects.get(id_product=id_product)

        bidding = int(request.POST["bidding_value"]) #get value bidding by user

        all_bids = Bid.objects.filter(product=product_details) # get all bids from product

        try:
            highest_bidding = max(all_bids, key=lambda bid: bid.bidding_value)
            high_bidding = highest_bidding.bidding_value
        except ValueError: #if there are no bids yet
            high_bidding = 0 #create a temp value for bidding = 0

        if bidding >= product_details.min_bidding and bidding > high_bidding: #check if bidding is valid
            bid = Bid(  product=product_details,
                        bidder=request.user,
                        bidding_value= bidding,
                        winning_bid= False
            )

            bid.save()

            return HttpResponseRedirect(reverse("product", kwargs={"id_product": id_product}))

        else: # if the bid was not valid, return message to user

            if high_bidding == 0:
                min_b = product_details.min_bidding
            else:
                min_b = max(product_details.min_bidding, high_bidding) + 1

            message =  f"INVALID BID! You need to bid at least {min_b} galleons."

            return product(request, id_product, message)

def comment(request, id_product):
    if request.method == "POST":
        comment_user = request.POST["comment"]

        c = ListingComments(product= Listing.objects.get(id_product=id_product),
                                comment = comment_user,
                                buyer = request.user)

        c.save() # save comment

        return HttpResponseRedirect(reverse("product", kwargs={"id_product": id_product}))

def pause_bidding(request, id_product):
    if request.method == "POST":
        product = Listing.objects.get(id_product=id_product) # create a product based on product_id

        try:
            product.status = "PAU"
            product.save()
        except Listing.DoesNotExist:
            pass #does nothing

        return HttpResponseRedirect(reverse("product", kwargs={"id_product": id_product}))

def active_bidding(request, id_product):
    if request.method == "POST":
        product = Listing.objects.get(id_product=id_product) # create a product based on product_id

        try:
            product.status = "ACT"
            product.save()
        except Listing.DoesNotExist:
            pass #does nothing

        return HttpResponseRedirect(reverse("product", kwargs={"id_product": id_product}))

def end_bidding(request, id_product):
    if request.method == "POST":
        product = Listing.objects.get(id_product=id_product) # create a product based on product_id

        all_bids = Bid.objects.filter(product=product) # get all bids from product

        try:
            highest_bidding = max(all_bids, key=lambda bid: bid.bidding_value) #finds the highest bidding

            highest_bidding.winning_bid = True #set bidding as winning bid
            highest_bidding.save() # save highest bidding

            product.status = "SOL" #changes status of listing to SOLD
            product.save() # save listing as SOLD

        except (Listing.DoesNotExist, Bid.DoesNotExist):
            pass #does nothing

        return HttpResponseRedirect(reverse("product", kwargs={"id_product": id_product}))

def selling(request):
    return render(request, "auctions/selling.html", {
        "selling": Listing.objects.filter(seller = request.user)
    })
