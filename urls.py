from django.conf.urls import url

from . import views
from .views import listing, parcategorie



urlpatterns = [
    url(r'^$', listing, name='rcindex'),

    #     url(r'^dossierslist/$', dossier_new, name='dossierslist'),
    url(r'^categorie/(?P<catego>[-\w]+)/$', parcategorie , name='rcindexcatego'),
    #     url(r'^(?P<pid>[-\w]+)/dossier/new/$', views.dossier_new, name='dossier_new'),
]


