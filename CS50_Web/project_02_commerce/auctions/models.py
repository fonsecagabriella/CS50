from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=48)
    email = models.EmailField(max_length=48)


class Listing(models.Model):
    id_product = models.AutoField(primary_key=True)

    title = models.CharField(max_length=24)

    description = models.TextField(max_length=1024)

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")

    min_bidding = models.DecimalField(max_digits=10, decimal_places=2)

    date_added = models.DateTimeField(auto_now_add=True)

    date_end_bidding = models.DateField()

    photo_url = models.URLField()

    class ListingStatus(models.TextChoices):
        ACTIVE = 'ACT',
        PAUSED = 'PAU',
        SOLD = 'SOL'

    status = models.CharField(
        max_length=3,
        choices=ListingStatus.choices,
        default=ListingStatus.PAUSED
    )

    class ListingCategory(models.TextChoices):
        BOOKS = 'BO',
        HOUSEHOLD = 'HH',
        ELECTRONICS = 'EL',
        OTHERS = 'OT'

    category = models.CharField(
        max_length=2,
        choices=ListingCategory.choices,
        default=ListingCategory.OTHERS
    )

    def __str__(self):
        return f"{self.title}, from {self.seller}. Status: {self.status}"



class Bid(models.Model):
    product = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="all_bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_bidders")
    bidding_value = models.DecimalField(max_digits=10, decimal_places=2)
    date_bidding = models.DateTimeField(auto_now_add=True)
    winning_bid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bidder} offers {self.bidding_value} on {self.product}"

class ListingComments(models.Model):
    product = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="all_comments")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.TextField(blank=True, max_length=140)
    date_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.buyer } commented on { self.product } on { self.date_comment }"

class Watchlist(models.Model):
    product = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watching")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")

    def __str__(self):
        return f"{self.product}, wachtlisted by {self.buyer}"

