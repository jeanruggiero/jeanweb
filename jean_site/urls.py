from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/tetracraft', views.tetracraft, name='tetracraft'),
    path('portfolio/personal_site', views.personal_site, name='personal_site'),
    path('portfolio/andrew_fabian_website', views.andrew_website, name="andrew_fabian_website"),
    path('portfolio/lighthouse', views.lighthouse, name='lighthouse'),
    path('portfolio/party_mode', views.party_mode, name="party_mode"),
    path('portfolio/brc_website', views.brc_website, name="brc_website"),
    path('portfolio/mission_compostable', views.mission_compostable, name="mission_compostable"),
    path('portfolio/ocularize', views.ocularize, name="ocularize"),
    path('contact', views.contact, name='contact'),
]
