from django.db import models

class Products(models.Model):
    """ Modelo del los Productos """
    
    #nombre
    name= models.CharField(max_length=20)

    #precio
    price = models.FloatField()

    #stock
    stock = models.PositiveIntegerField(default=0) 

    #descripcion
    description = models.TextField()

    #cuando se creo y se modifico
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Reuturn product name """
        return self.name