""" User admin Classes """

#django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#Models
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin """
    list_display = ('id', 'user_id', 'cart')
    
    list_display_links = ('id', 'user_id')
    
    list_editable = ('cart',)
    
    list_filter = (
        'created', 
        'modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user_id'), )
        }),
        ('Extra info', {
            'fields': (('cart'),)
        }),
        ('Metadata', {
            'fields': (('created', 'modified'), )
        }),
    )

    readonly_fields = ('created', 'modified', 'user_id')

class ProfileInLine(admin.StackedInline):
    """ Profile in-line admin for users """
    model = Profile
    verbose_name_plural = 'Profiles'
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    """ add profile admin to base user admin """
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)