from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
