from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finche
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finche.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finche_id):
    finche = Finche.objects.get(id=finche_id)
    return render (request, 'finches/detail.html', {
        'finche': finche
    })

class FincheCreate(CreateView):
    model = Finche
    fields = '__all__'

class FincheUpdate(UpdateView):
    model = Finche
    fields = ['color', 'description']

class FincheDelete(DeleteView):
    model = Finche
    success_url = '/finches'
