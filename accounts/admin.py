
from django.contrib import admin

from accounts.models import Profile, Country

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbr', 'is_active']