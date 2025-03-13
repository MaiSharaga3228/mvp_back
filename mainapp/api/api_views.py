from rest_framework import viewsets, permissions

from mainapp.models import Category, Product, Cart
from mainapp.api.serializers import CategorySerializer, ProductSerializer, CartSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CartViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    # TODO: restrict access to carts
    # permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     user = self.request.user
    #     return user.carts.all()

