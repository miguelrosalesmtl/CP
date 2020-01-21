from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework import generics, mixins, viewsets, views
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .serializers import (
    OrderSerializer,
    OrderDetailSerializer,
    FoodSerializer)
from .models import Order, OrderDetail, Food


class FoodAPIView(generics.ListAPIView):
    ''' Food API View '''
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class OrderLDRViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    ''' Order View set to list, retrieve, update and destroy orders '''

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'status']

    @action(detail=False, methods=['GET'])
    def cart(self, request):
        obj, created = Order.objects.get_or_create(
            user=request.user,
            status=Order.CART)
        serializer = OrderSerializer(obj)
        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def send_order(self, request, pk=None):
        ''' Converts cart into  '''

        obj = get_object_or_404(Order, pk=pk)
        if obj.status != Order.CART:
            return Response(
                {"message": "Invalid operation on order"},
                status.HTTP_400_BAD_REQUEST)
        obj.status = Order.NEW
        obj.created = now()
        # reverify one last time
        obj.calculate_totals()
        obj.save()
        return Response({"message": "Order sent!"}, status.HTTP_200_OK)

    def get_queryset(self):
        return Order.objects.exclude(status=Order.CART)


class OrderDetailCDViewSet(
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    ''' Order detail View set to create, destroy, list, update '''

    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
