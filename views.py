from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from RCaulet.models import Oeuvre, Categorie



def listing(request):
    categories = Categorie.objects.all()
    oeuvres = Oeuvre.objects.filter(parent__id=1).filter(id__gt=1)

    return render(request, 'rcindex.html', {'oeuvres': oeuvres, 'categories': categories}, )


def parcategorie(request, catego):
    parents = Oeuvre.objects.filter(categorie__id=catego).filter(parent__id=1).filter(id__gt=1)
    categorie = Categorie.objects.get(id=catego)
    if categorie.id == 5:
        return render(request, 'rcindexlivrets.html', {'oeuvres': parents} )
    else:
        return render(request, 'rcindexcatego.html', {'oeuvres': parents, 'categorie': categorie} )

def slideshow(request, oeuvre):
    parents = Oeuvre.objects.filter(id= oeuvre)
    return render(request, 'rcslide.html', {'oeuvres': parents,} )



