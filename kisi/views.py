from django.shortcuts import render
from rest_framework import generics
from . import Serializers
from . import models


# Create your views here.
class CreateProduct(generics.CreateAPIView):
    serializer_class = Serializers.ProductSerializer
    queryset = models.KProduct.objects.all()


class CreateReview(generics.CreateAPIView):
    serializer_class = Serializers.ReviewSerializer
    queryset = models.KReview.objects.all()


class ListProduct(generics.ListAPIView):
    serializer_class = Serializers.ProductSerializer
    queryset = models.KProduct.objects.all()


class ListReview(generics.ListAPIView):
    serializer_class = Serializers.ReviewSerializer
    queryset = models.KReview.objects.all()