
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_note", views.new_note, name="new_note"),
    path("following", views.following, name="following"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("comment_note", views.comment_note, name="comment_note"),
    path("like_note/<str:note_id>", views.like_note, name="like_note"),
    path("note/<str:note_id>", views.note, name="note"),
    path("edit_note/<str:note_id>", views.edit_note, name="edit_note"),
    path("save_edit_note", views.save_edit_note, name="save_edit_note"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("follow/<str:profile_to_follow>", views.follow, name="follow"),

]
