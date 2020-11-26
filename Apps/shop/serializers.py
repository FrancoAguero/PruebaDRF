
#Django
from django.contrib.auth.models import User, Group
from rest_framework import serializers


#Locasl Models
from Apps.shop.models import Products
from Apps.profile.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'description', 'stock']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['cart']

class QuantityCartSerializer(serializers.ModelSerializer):

    quantity = serializers.IntegerField()
