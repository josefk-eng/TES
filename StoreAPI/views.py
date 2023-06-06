from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from . import models, Serializers
from rest_framework.response import Response
from .utils import custom_exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status


# Create your views here.
class CreateProduct(generics.CreateAPIView):
    serializer_class = Serializers.ProductSerializer
    queryset = models.Product.objects.all()


class ListProduct(generics.ListAPIView):
    serializer_class = Serializers.ProductSerializer
    queryset = models.Product.objects.all()


class GetProduct(generics.RetrieveAPIView):
    serializer_class = Serializers.ProductSerializer
    queryset = models.Product.objects.all()


class UpdateProduct(generics.UpdateAPIView):
    serializer_class = Serializers.ProductSerializer
    queryset = models.Product.objects.all()


class DeleteProduct(generics.DestroyAPIView):
    serializer_class = Serializers.ProductSerializer
    queryset = models.Product.objects.all()


class ListTags(generics.ListAPIView):
    serializer_class = Serializers.TagSerializer
    queryset = models.Tag.objects.all()


class GetBanner(generics.RetrieveAPIView):
    serializer_class = Serializers.BannerSerializer
    queryset = models.Banner.objects.all()


class GetDistricts(generics.ListAPIView):
    serializer_class = Serializers.DistrictSerializer
    queryset = models.District.objects.all()


class GetDivision(generics.ListAPIView):
    serializer_class = Serializers.DivisionSerializer
    queryset = models.Division.objects.all()


class GetParish(generics.ListAPIView):
    serializer_class = Serializers.ParishSerializer
    queryset = models.Parish.objects.all()


class GetVillage(generics.ListAPIView):
    serializer_class = Serializers.VillageSerializer
    queryset = models.Village.objects.all()


class GetStreet(generics.ListAPIView):
    serializer_class = Serializers.StreetSerializer
    queryset = models.Street.objects.all()


class AddUser(generics.CreateAPIView):
    serializer_class = Serializers.UserSerializer
    queryset = models.UserToken.objects.all()


class AddOrder(generics.CreateAPIView):
    serializer_class = Serializers.OrderSerializer
    queryset = models.Order.objects.all()


@api_view(['POST'])
def addressing(request):
    query = request.data["type"]
    quota = request.data["quota"]
    if query == "district":
        districts = models.District.objects.all()
        serializer = Serializers.DistrictSerializer(districts,many=True)
        return Response(serializer.data)
    elif query == "division":
        division = models.Division.objects.filter(district=quota)
        serializer = Serializers.DivisionSerializer(division, many=True)
        return Response(serializer.data)
    elif query == "parish":
        parish = models.Parish.objects.filter(division=quota)
        serializer = Serializers.ParishSerializer(parish, many=True)
        return Response(serializer.data)
    elif query == "village":
        village = models.Village.objects.filter(parish=quota)
        serializer = Serializers.VillageSerializer(village,many=True)
        return Response(serializer.data)
    elif query == "street":
        street = models.Street.objects.filter(village=quota)
        serializer = Serializers.StreetSerializer(street,many=True)
        return Response(serializer.data)
    else:
        return custom_exception_handler(APIException(detail="Unknown AddressType", code=status.HTTP_400_BAD_REQUEST), context={"request": request})