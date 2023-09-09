import json

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator #Required to implement pagination


from .models import User, Note, Comments


def index(request):

    notes = Note.objects.all().order_by('-created')
    paginator = Paginator(notes, 10) # Show 10 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
            "page_obj": page_obj,
            "title_notes": "🦉 All Notes"
        })

@login_required
def following(request):

    f_users = User.objects.get(username=request.user.username)

    notes_following = Note.objects.filter(owner__in=request.user.following.all()).order_by('-created')

    paginator = Paginator(notes_following, 10) # Show 10 notes per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, "network/following.html", {
            "page_obj": page_obj,
            "title_notes": "🦉 What The Wizards You Follow Are Saying"
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new_note(request):
    if request.method == "POST":
        # get data from form
        note_content = request.POST["note_content"]

        # create a new note
        new_note = Note(note_content=note_content,
                        owner= request.user )
        # save note
        new_note.save()

        return HttpResponseRedirect(reverse("index"))

@csrf_exempt
@login_required
def like_note(request, note_id):
    # Query for requested note
    try:
        note = Note.objects.get(note_id=note_id)
        user_liking = User.objects.get(username=request.user.username)
    except Note.DoesNotExist:
        return JsonResponse({"error": "Note not found."}, status=404)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)


     # Check if the user is among the likers for the note
    is_liked = note.likers.filter(pk=user_liking.pk).exists()

    # Change the status of a Liker in a note
    if request.method == "PUT":
        if is_liked:
            note.likers.remove(user_liking)
        else:
            note.likers.add(user_liking)

        return JsonResponse({
                "likers": note.likers.count()
            }, status=200)

    # Note must be changed via PUT
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)

@csrf_exempt
@login_required
def follow(request, profile_to_follow):
    # Query for requested profile
    try:
        followed = User.objects.get(username=profile_to_follow)
        follower = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)

    # Change the status of following / not following
    if request.method == "PUT":
        if follower.is_following(followed):
            follower.unfollow(followed)
        else:
            follower.follow(followed)

        return JsonResponse({
                "followers": followed.followers.count(),
                "following": followed.following.count()
            }, status=200)

    # Profile followers must be changed via PUT
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)


def profile(request, username):
    profile = User.objects.get(username=username)
    notes = Note.objects.filter(owner=profile).order_by('-created')

    paginator = Paginator(notes, 10) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #Create the title for the notes based on user's name
    title_notes = f" {profile.username}'s notes"

    #check if is following
    if request.user.is_authenticated:
        is_following = request.user.is_following(profile)
    else:
        is_following = False

    #print(notes)
    #return HttpResponseRedirect(reverse("profile", kwargs={"username": profile.username}))
    return render(request, "network/profile.html", {
                                                    "profile": profile,
                                                    "page_obj": page_obj,
                                                    "title_notes": title_notes,
                                                    "is_following": is_following })

@login_required
def edit_profile(request):
    if request.method == "POST":

        profile = User.objects.get(username=request.user.username)
        # Attempt to sign user in
        profile.bio = request.POST["bio"]
        profile.emoji = request.POST["emoji"]
        profile.first_name = request.POST["first_name"]
        profile.last_name = request.POST["last_name"]

        profile.save()

        # return render(request, "network/profile.html", {"profile": profile, "all_notes": Note.objects.filter(owner=profile),
        #                                "is_following": request.user.is_following(profile)})

        return HttpResponseRedirect(reverse("profile", kwargs={"username": profile.username}))

    else:
        profile = User.objects.get(username=request.user.username)
        return render(request, "network/edit_profile.html", {"profile": profile })


def note(request, note_id):
    if request.method == "GET":
        note = Note.objects.get(note_id=note_id)
        comments = Comments.objects.filter(note_id=note).order_by('-date')

        return render(request, "network/note.html", {
            "note": note, "comments": comments
        })


def comment_note(request):
    if request.method == "POST":
        # get data from form
        comment_text = request.POST["comment-text"]
        note_id = request.POST["note_id"]
        note = Note.objects.get(note_id=note_id)

        # create a new comment
        new_comment = Comments(comment=comment_text,
                        commentator = request.user,
                        note_id =note )
        # save comment
        new_comment.save()

    note = Note.objects.get(note_id=note_id)
    comments = Comments.objects.filter(note_id=note).order_by('-date')

    return HttpResponseRedirect(reverse('note', args=[note_id]), {
            "note": note, "comments": comments
        })

@csrf_exempt
@login_required
def edit_note(request, note_id):
    # Query for requested note
    try:
        note = Note.objects.get(note_id=note_id)
        owner = User.objects.get(username=request.user.username)
    except Note.DoesNotExist:
        return JsonResponse({"error": "Note not found."}, status=404)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)

    print(request.method)

    if request.method == "PUT":
        print("PUT")

        data = json.loads(request.body)
        new_note = data.get("edited_note_text")

        note.note_content = new_note
        note.save()

        name_id = "#" + note_id

        print(f"This is the id: {name_id}")

        return JsonResponse({
                "note_content": note.note_content,
                "name_id": name_id
            }, status=200)

    elif request.method == "GET":
        return JsonResponse({
                "note_content": note.note_content
            }, status=200)

    # Note must be changed via PUT
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)


@csrf_exempt
@login_required
def save_edit_note(request):

    print(request.method)

    if request.method == "PUT":
        print("PUT")

        data = json.loads(request.body)
        new_note = data.get("edited_note_text")
        note_id = data.get("note_id")

        # Query for requested note
        try:
            note = Note.objects.get(note_id=note_id)
        except Note.DoesNotExist:
            return JsonResponse({"error": "Note not found."}, status=404)


        note.note_content = new_note
        note.save()

        name_id = "#note_" + note_id

        print(f"This is the id: {name_id}")

        return JsonResponse({
                "note_content": note.note_content,
                "name_id": name_id
            }, status=200)

    # Note must be changed via PUT
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)