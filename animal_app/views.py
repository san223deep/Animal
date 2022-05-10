from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import AnimalForm
from .models import AnimalList, Animals, Breed
from django.contrib import messages


def index(request):

    animal_list = AnimalList.objects.all()
    form = AnimalForm()
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            row = form.save()
            print(row)
            return render(request, 'animal_app/new_row.html', {'row': row})
        else:
            return render(request, 'animal_app/index.html')

    context = {
        'animal_list': animal_list,
        'form': form,
    }

    return render(request, 'animal_app/index.html', context)


def get_animals(request):
    animals = Animals.objects.all()
    context = {
        'animals': animals
    }
    return render(request, 'animal_app/animal_input.html', context)


def get_breeds(request):
    animal_pk = request.GET.get('animal')
    breeds = Breed.objects.filter(animal__pk=animal_pk)
    context = {
        'breeds': breeds
    }
    return render(request, 'animal_app/breed_input.html', context)


def remove_row(request, pk):
    AnimalList.objects.filter(pk=pk).delete()
    context = {
        'animal_list': AnimalList.objects.all()
    }
    return render(request, 'animal_app/animal_list.html', context)
