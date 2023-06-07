from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CreateProduct,
    ListProduct,
    UpdateProduct,
    DeleteProduct,
    ListTags,
    GetBanner,
    GetProduct,
    addressing,
    GetDistricts,
    GetDivision,
    GetParish,
    GetVillage,
    GetStreet,
    AddUser,
    AddOrder,
    search
)

urlpatterns = [
    path(r'api-token-auth/', TokenObtainPairView.as_view()),
    path(r'api-token-refresh/', TokenRefreshView.as_view()),
    path(r'addP', CreateProduct.as_view()),
    path(r'allProducts', ListProduct.as_view()),
    path(r'product/<pk>', GetProduct.as_view()),
    path(r'update/<pk>', UpdateProduct.as_view()),
    path(r'delete/<pk>', DeleteProduct.as_view()),
    path(r'tags', ListTags.as_view()),
    path(r'banner/<pk>', GetBanner.as_view()),
    path('addressing', addressing, name='addressing'),
    path(r'district', GetDistricts.as_view(), name='district'),
    path(r'division', GetDivision.as_view(), name='division'),
    path(r'parish', GetParish.as_view(), name='parish'),
    path(r'village', GetVillage.as_view(), name='village'),
    path(r'street', GetStreet.as_view(), name='street'),
    path(r'addUser', AddUser.as_view(), name='addUser'),
    path(r'order', AddOrder.as_view(), name='order'),
    path('search/<str:query>', search,name='search'),
]
