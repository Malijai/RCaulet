from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from RCaulet.models import Oeuvre, Categorie



def listing(request):
    categories = Categorie.objects.exclude(livret=Categorie.PAS)
    oeuvres = Oeuvre.objects.filter(parent__id=1).filter(id__gt=1)
    return render(request, 'rcindex.html', {'oeuvres': oeuvres, 'categories': categories}, )


def parcategorie(request, catego):
    parents = Oeuvre.objects.filter(categorie__id=catego).filter(parent__id=1).filter(id__gt=1)
    categorie = Categorie.objects.get(id=catego)
    categories = Categorie.objects.exclude(livret=Categorie.PAS)
    if categorie.livret == Categorie.AL:
        return render(request, 'rcindexlivrets.html', {'oeuvres': parents, 'categorie': categorie, 'categories': categories} )
    else:
        return render(request, 'rcindexcatego.html', {'oeuvres': parents, 'categorie': categorie, 'categories': categories} )


def slideshow(request, oeuvre):
    parent = Oeuvre.objects.get(id=oeuvre)
    categories = Categorie.exclude(livret=Categorie.PAS)
    return render(request, 'rcslide.html', {'oeuvre': parent, 'categories': categories} )



