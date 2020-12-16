from rest_framework import serializers

from .models import auction, bidder

# Serializer Validator for Auction.

class auctionserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True)
    

    class Meta:
        model = auction
        fields = '__all__'


# Serializer Validator for bidder

class bidderserializer(serializers.ModelSerializer):
    auctioneer = serializers.UUIDField(required=True)
    price = serializers.FloatField(required=True)
    modified_at = serializers.DateTimeField(required=False)

    class Meta:
        model = bidder
        fields = '__all__'
