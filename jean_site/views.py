from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def home(request):
    return render(request, 'jean_site/home.html')


def resume(request):
    return render(request, 'jean_site/resume.html')


def portfolio(request):
    return render(request, 'jean_site/portfolio.html')


def tetracraft(request):
    return render(request, 'jean_site/portfolio/tetracraft.html')


def personal_site(request):
    return render(request, 'jean_site/portfolio/personal_site.html')


def andrew_website(request):
    return render(request, 'jean_site/portfolio/andrew_website.html')


def lighthouse(request):
    return render(request, 'jean_site/portfolio/lighthouse.html')


def party_mode(request):
    return render(request, 'jean_site/portfolio/party_mode.html')


def brc_website(request):
    return render(request, 'jean_site/portfolio/brc_website.html')


def mission_compostable(request):
    return render(request, 'jean_site/portfolio/mission_compostable.html')


def contact(request):
    return render(request, 'jean_site/contact.html')
