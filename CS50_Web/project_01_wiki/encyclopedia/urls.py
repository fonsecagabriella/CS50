from django.urls import path
from . import views


# the function that define the views are in views.NAME_FUNCTION
urlpatterns = [
    path("", views.index, name="index"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("search", views.search, name="search"),
    path("wiki/<str:title>", views.get_entry, name="entry"),
    path("edit/<str:title>", views.edit_entry, name="edit_entry")
]
