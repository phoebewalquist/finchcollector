from django.shortcuts import render

finches = [
  {'name': 'Peter', 'breed': 'Purple finch', 'description': 'purple and cool', 'age': 5},
  {'name': 'Sam', 'breed': 'European goldfinch', 'description': 'silly and playful', 'age': 5},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })