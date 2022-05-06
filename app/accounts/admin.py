from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as GenericUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Client, Helper


@admin.register(User)
class UserAdmin(GenericUserAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    search_fields = ['name', 'email']
    ordering = ['-id']

    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'birth_data', 'email', 'password1', 'password2'),
        }),
    )


@admin.register(Helper)
class HelperAdmin(GenericUserAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    search_fields = ['name', 'email']
    ordering = ['-id']

    fieldsets = (
        (None, {'fields': ('name', 'picture', 'document', 'birth_data', 'email', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', ),
        }),
        ('Endereço', {'fields': ['country', 'zipcode', 'state', 'city', 'number', 'complement', 'address', 'neighborhood']})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'birth_data', 'email', 'password1', 'password2'),
        }),
    )


@admin.register(Client)
class ClientAdmin(GenericUserAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    search_fields = ['name', 'email']
    ordering = ['-id']

    fieldsets = (
        (None, {'fields': ('name', 'picture', 'document', 'birth_data', 'email', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', ),
        }),
        ('Endereço', {'fields': ['country', 'zipcode', 'state', 'city', 'number', 'complement', 'address', 'neighborhood']})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'birth_data', 'email', 'password1', 'password2'),
        }),
    )
