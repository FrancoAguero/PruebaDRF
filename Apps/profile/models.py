""" Users Models """

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Modelo del Perfil """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #el carro se guarda tipo json pero en strig despues cuando traigo el dato lo parseo
    cart = models.CharField(default='{"cart": []}', max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return username """
        return self.user.username