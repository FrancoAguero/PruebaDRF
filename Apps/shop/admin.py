""" Products admin classes """

#django
from django.contrib import admin


#models
from .models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin """
    list_display = ('id', 'name', 'price', 'description', 'stock')
    
    list_display_links = ('id',)
    
    list_editable = ('description', 'price', 'stock', 'name')
    
    search_fields = ('name',)
    
    list_filter = (
        'created', 
        'modified',
    )

    fieldsets = (
        ('Products', {
            'fields': (('name', 'description'), ('price', 'stock'),)
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        }),
    )

    readonly_fields = ('created', 'modified')

