from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Animals(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Breed(models.Model):
    animal = models.ForeignKey('animal_app.Animals', on_delete=models.CASCADE, related_name='breeds')
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} - {self.animal.name}'


class AnimalList(models.Model):
    animal = models.ForeignKey('animal_app.Animals', on_delete=models.CASCADE, related_name='in_list')
    breed = models.ForeignKey('animal_app.Breed', on_delete=models.CASCADE, related_name='in_list')
    date = models.DateField()

    class Meta:
        ordering = ['-pk']

