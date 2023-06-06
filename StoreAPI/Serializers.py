from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserToken
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Division
        fields = '__all__'


class ParishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parish
        fields = '__all__'


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Village
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Street
        fields = '__all__'
