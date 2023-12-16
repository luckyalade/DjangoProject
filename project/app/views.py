from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from app.form import SignUpForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')


def UserForm(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'profile.html', context)
