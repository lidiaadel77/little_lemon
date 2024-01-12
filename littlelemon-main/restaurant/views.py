from django.shortcuts import render
from rest_framework import viewsets , generics
from django.contrib.auth.models import User
from .serializers import UserSerializer , MenuItemSerializer , BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
   return Response({"message":"This view is protected"})

def index(request):
   return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

class MenuItemsView(generics.ListCreateAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = Booking
    permission_classes = [IsAuthenticated,]