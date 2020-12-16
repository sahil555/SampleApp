from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
from django.utils import timezone 


# Model for Auction 

class auction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    auction_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)


    objects = models.Manager()

    def __str__(self):
        return '%s'%self.auction_id


# Model for bidder 

class bidder(models.Model):
    auctioneer = models.UUIDField()
    bidder_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(null=True)

    objects = models.Manager()

    def __str__(self):
        return '%s'%self.bidder_id