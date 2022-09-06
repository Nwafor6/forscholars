from django.contrib import admin
from .models import CustomUser, Profile
from django.contrib.auth.admin import UserAdmin
# # Register your models here.


admin.site.register(Profile)

#######################


from . import models 
from . import forms 
# Register your models here.

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser

    ordering = ["email"]
    list_display = ["email", "is_staff", "is_active","is_superuser"]
    search_fields = ["email"]
    
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        ('Details', {
            "fields": (
                'first_name', 'last_name', 'slug'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_active'
            ),
        }),
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
    }),
)
