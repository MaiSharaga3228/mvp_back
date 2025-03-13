from mainapp.models import Category, Product, Cart
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description']


class CartSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'products']
        depth = 1

    def get_owner(self, obj):
        return obj.owner.username
