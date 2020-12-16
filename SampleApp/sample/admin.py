from django.contrib import admin

from .models import auction,bidder
# Register your models here.


# auction admin panel VIEW

@admin.register(auction)
class auctionadmin(admin.ModelAdmin):
    list_display = ('user','auction_id','created_at')
    fields = [('user','auction_id')]
    readonly_fields = ["created_at"]

    class Meta:
        ordering=['-created_at']
        
# auction bidder panel VIEW


@admin.register(bidder)
class bidderadmin(admin.ModelAdmin):
    list_display = ('auctioneer','bidder_id','price','created_at','modified_at')
    fields = [('auctioneer','bidder_id','price','modified_at')]
    readonly_fields = ["created_at"]

    class Meta:
        ordering=['-price']