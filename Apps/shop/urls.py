""" Shop Urls """

#Django
from django.urls import path
from Apps.shop import views
from django.urls import include, path


# Django Rest Framwork
from rest_framework import routers


urlpatterns = [
    path(
        route='', 
        view=views.ProductView.as_view(),
        name='product'
    ),
    
    path(
        route='cart/',
        view=views.CartView.as_view(),
        name='cart'
    ),

    path(
        route='cart/add/<int:id>/',
        view=views.AddProductCart.as_view(),
        name='add_cart'
    ),

    path(
        route='cart/delete/<int:id>/',
        view=views.DeleteProductCart.as_view(),
        name='delete_cart'
    ),

    path(
        route="cart/buy/<int:id>/",
        view=views.ComprarProducto.as_view(),
        name="buy"
    ),

    path(
        route="cart/succefully_buy/",
        view=views.CompraExitosa.as_view(),
        name="succefully_buy"
    ),
]