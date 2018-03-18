from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from RCaulet.models import Oeuvre, Categorie



def listing(request):
#    if request.user.is_authenticated:
    oeuvres = Oeuvre.objects.all()
#    paginator = Paginator(oeuvres_list, 5) # Show 5 post par page
#    page = request.GET.get('page')
#    try:
#        oeuvres = paginator.page(page)
#    except PageNotAnInteger:
#            # If page is not an integer, deliver first page.
#            oeuvres = paginator.page(1)
#    except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
#            oeuvres = paginator.page(paginator.num_pages)
    oeuvres = Oeuvre.objects.filter(parent__id=0).filter(id__gt=0)

    return render(request, 'rcindex.html', {'oeuvres': oeuvres}, )


def parcategorie(request, catego):
    parents = Oeuvre.objects.filter(categorie__id=catego).filter(parent__id=0).filter(id__gt=0)
    categorie = Categorie.objects.get(id=catego)
    if categorie.id == 5:
        return render(request, 'rcindexlivrets.html', {'oeuvres': parents} )
    else:
        return render(request, 'rcindexcatego.html', {'oeuvres': parents, 'categorie': categorie} )

def slideshow(request, oeuvre):
    parents = Oeuvre.objects.filter(id= oeuvre)
    return render(request, 'rcslide.html', {'oeuvres': parents,} )



