from rest_framework import status,permissions



from rest_framework.response import Response

from . import serializer


from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view , permission_classes

from .models import User,auction,bidder

# VIEW for auction query for maximum price bid 


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def auctionview(request):
    if request.data:
        data = request.data
        auct_id = data['auction_id']

        if auct_id:
            bidderinfo = bidder.objects.filter(auctioneer=auct_id).order_by('-price').first()

            # bd = bidderinfo.aggregate(max('price'))
            bid = {
                    "auctioneer": str(bidderinfo.auctioneer),
                    "bidder_id": str(bidderinfo.bidder_id),
                    "price": bidderinfo.price 
                    }
                
            print(bid)
            return Response({'data':bid},status=status.HTTP_200_OK)
        else:
            return Response({'Error': auct_id},status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'message':f'null data requested {request.data}'},status=status.HTTP_400_BAD_REQUEST)


# auctions LIST for a particular time are Live

@api_view(['GET'])
def auctionlist(request):
    # lguser = request.user.username

    auctionlists = auction.objects.all()
    listauct = []
    for ob in auctionlists:
        listauct.append(ob.auction_id)

    return Response(listauct,status=status.HTTP_200_OK)


# View for creating a view in real time it will reflect in max PRICE auction LIST view

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def createbid(request):
    if request.data:
        data = request.data

        auctioninstance = auction.objects.filter(auction_id=data['auctioneer']).first()
        
        data.update(auctioneer=auctioninstance.auction_id)

        biderserial = serializer.bidderserializer(data=data)
        if biderserial.is_valid():
            biderserial.save()
            resp = {
                biderserial.validated_data.get('auctioneer'),
                biderserial.validated_data.get('price')
                }
            return Response(resp,status=status.HTTP_200_OK)
        else:
            return Response(biderserial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response({'Error': f'{request.data } Null Data requested'},status=status.HTTP_400_BAD_REQUEST)


            

