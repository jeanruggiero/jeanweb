from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'jean_site/home.html')


def resume(request):
    return render(request, 'jean_site/resume.html')


def portfolio(request):
    return render(request, 'jean_site/portfolio.html')


def tetracraft(request):
    return render(request, 'jean_site/portfolio/tetracraft.html')
