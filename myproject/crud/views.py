from django.shortcuts import render
from .forms import StudentForm
from .models import Student

# Create your views here.
def add(request):

    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form':form})

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')