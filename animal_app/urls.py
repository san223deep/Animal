from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('get_animals', views.get_animals, name='get_animals'),
    path('get_breeds', views.get_breeds, name='get_breeds'),
    path('remove_row/<pk>', views.remove_row, name='remove_row'),
]