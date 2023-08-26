from django.contrib import admin
from .models import Listing, Bid, ListingComments, Watchlist, User

# Register your models here.


admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(ListingComments)
admin.site.register(Watchlist)
admin.site.register(User)
