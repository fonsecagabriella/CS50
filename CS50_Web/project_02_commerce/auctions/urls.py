from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path('login/<str:next>/', views.login_view, name='login_with_next'),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("product/<str:id_product>", views.product, name="product"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("active", views.active, name="active"),
    path("select_category", views.select_category, name="select_category"),
    path("add_watchlist/<str:id_product>", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist/<str:id_product>", views.remove_watchlist, name="remove_watchlist"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("comment/<str:id_product>", views.comment, name="comment"),
    path("bidding/<str:id_product>", views.bidding, name="bidding"),
    path("pause_bidding/<str:id_product>", views.pause_bidding, name="pause_bidding"),
    path("active_bidding/<str:id_product>", views.active_bidding, name="active_bidding"),
    path("end_bidding/<str:id_product>", views.end_bidding, name="end_bidding"),
    path("selling", views.selling, name="selling")

]
