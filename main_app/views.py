# from .forms import FeedingForm, redirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finche, Toy
from .forms import FeedingForm
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
    id_list = finche.toys.all().values_list('id')
    toys_finche_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render (request, 'finches/detail.html', {
        'finche': finche, 'feeding_form': feeding_form,
        'toys': toys_finche_doesnt_have
    })

class FincheCreate(CreateView):
    model = Finche
    fields = [ 'breed', 'description', 'color']

class FincheUpdate(UpdateView):
    model = Finche
    fields = ['color', 'description']

class FincheDelete(DeleteView):
    model = Finche
    success_url = '/finches'

def add_feeding(request, finche_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finche_id = finche_id
        new_feeding.save()
    return redirect('detail', finche_id=finche_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, finche_id, toy_id):
   Finche.objects.get(id=finche_id).toys.add(toy_id)
   return redirect('detail', finche_id=finche_id)
