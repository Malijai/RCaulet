from django.conf.urls import url

from . import views
from .views import listing, parcategorie, slideshow



urlpatterns = [
    url(r'^$', listing, name='rcindex'),
    url(r'^illustration/(?P<oeuvre>[-\w]+)/$', slideshow, name='rcslide'),
    url(r'^livrets/(?P<catego>[-\w]+)/$', parcategorie, name='rcindexlivrets'),
    url(r'^categorie/(?P<catego>[-\w]+)/$', parcategorie , name='rcindexcatego'),
    #     url(r'^(?P<pid>[-\w]+)/dossier/new/$', views.dossier_new, name='dossier_new'),
]



