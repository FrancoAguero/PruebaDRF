""" Users View """
#Django
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

#Serializers
from Apps.shop.serializers import UserSerializer, ProductSerializer, CartSerializer

#Locals Models
from Apps.shop.models import Products
from Apps.profile.models import Profile

#Utilities
import json


class UserViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """ User Detail view """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """ CArt Detail view """
    queryset = Profile.objects.all()
    serializer_class = CartSerializer


class ProductView(LoginRequiredMixin, APIView):
    """ Lista de los productos """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/products.html'
    
    def get(self, request):
        #obtengo los todos los productos disponibles
        queryset = Products.objects.all()

        serializer = ProductSerializer(queryset, many=True)

        #retorno los datos
        return Response({'serializer': serializer.data })


class CartView(LoginRequiredMixin, APIView):
    """ Vista del Carro"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cart/cart.html'

    def get(self, request):
        """ Ver los productos que 
            estan en el carro del perfil
            que esta logeado """
        
        #traigo los datos del perfil
        queryset = Profile.objects.get(user=self.request.user)
        #parceo el carro que esta en string
        data = json.loads(queryset.cart)

        queryset.cart = []
        #compruebo que el carro tenga productos
        if data["cart"]:
            for item in data["cart"]:
                product = Products.objects.get(id=item['id'])
                product.quantity = item['quantity']
                serializer = ProductSerializer(product)
                queryset.cart.append(product)

        #retorno los datos con los productos
        return Response({'queryset': queryset})

class AddProductCart(LoginRequiredMixin, APIView):
    """ Añade un producto a carro del usuario """

    def post(self, request, id):
        #traigo el carro del perfil
        queryset = Profile.objects.get(user=self.request.user)
        
        data = json.loads(queryset.cart)

        check_id = False
        #compruebo que el producto agregado no es en el carro
        for product in data["cart"]:
            if product["id"] == id:
                check_id = True
                break
                
        if not check_id:
            #agrego el id del producto
            quantity = request.POST["quantity"]
            new_product = {"id": id, "quantity": int(quantity)}
            data["cart"].append(new_product)

            #guardo los datos
            queryset.cart = str(data).replace("'", '"')
            queryset.save()
        
        #retorno para la pagina de productos
        return redirect('shop:cart')

class DeleteProductCart(LoginRequiredMixin, APIView):
    """ Eliminar un producto del carro del usuario """
    
    def post(self, request, id):
        #traigo el carro del perfil
        queryset = Profile.objects.get(user=self.request.user)
        
        #saco el id del producto que se quiere eliminar
        data = json.loads(queryset.cart)

        for product in data["cart"]:
            if product["id"] == id:
                data["cart"].remove(product)

        #guardo los datos
        queryset.cart = str(data).replace("'", '"')
        queryset.save()
        
        #retorno hacia la pagina del carro
        return redirect('shop:cart')


class ComprarProducto(LoginRequiredMixin, APIView):
    """ Hacer la compra de los productos que estan en el carro """

    def post(self, request, id):
        #traigo el carro del perfil
        queryset = Profile.objects.get(user=self.request.user)
        data = json.loads(queryset.cart)

        if data["cart"]:
            for product_data in data["cart"]:
                product = Products.objects.get(id=product_data["id"])
                product.stock = product.stock - product_data["quantity"]
                product.save()
            
            queryset.cart = '{"cart": []}'
            queryset.save()
        
        return redirect('shop:succefully_buy')

class CompraExitosa(LoginRequiredMixin, APIView):
    "Mostrar mensaje que la compra fue hecha"
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cart/succefully_buy.html'

    def get(self, request):
        return Response({"data": request})
        





        

        
