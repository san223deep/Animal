from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    fields = ('username', 'first_name', 'last_name', 'email', 'password', 'joined_date')


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal')


class AnimalListAdmin(admin.ModelAdmin):
    list_display = ('animal', 'breed', 'date')


admin.site.register(User, UserAdmin)
admin.site.register(Animals, AnimalAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(AnimalList, AnimalListAdmin)
