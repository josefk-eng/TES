from django.urls import path
from . import views
urlpatterns = [
    path('addProduct',views.CreateProduct.as_view(), name='addProduct'),
    path('addReview',views.CreateReview.as_view(), name='addReview'),
    path('getReview',views.ListReview.as_view(), name='getReview'),
    path('getProducts',views.ListProduct.as_view(), name='getProducts')
]