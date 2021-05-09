from django.urls import path
from . import views
from .views import parcategorie, slideshow


urlpatterns = [
    path('', views.listing, name='rcindex'),
    path('illustration/<int:oeuvre>/', slideshow, name='rcslide'),
    path('livrets/<int:catego>/', parcategorie, name='rcindexlivrets'),
    path('categorie/<int:catego>/', parcategorie , name='rcindexcatego'),
]



