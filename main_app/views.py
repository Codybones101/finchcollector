from django.shortcuts import render


finches = [
  {'name': 'tommy', 'breed': 'goldfinch', 'description': 'beautiful yellow coloring', 'age': 2},
  {'name': 'argile', 'breed': 'crossbill', 'description': 'happy little guy', 'age': 1},
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
