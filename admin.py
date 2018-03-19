from django.contrib import admin

from .models import Categorie, Oeuvre, Theme


class OeuvreAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Les champs en gras sont obligatoires. Pour les livrets. Uploader la couverture dans les 2 champs et ensuite chaque page dans -Pour les pages des livrets-', {'fields': []}),
        ('Informations', {'fields': ['titre','periode', 'texte','dimension',]}),
        ('Classification', {'fields': [('categorie', 'theme', 'ordre'),]}),
        ('Fichiers ! ATTENTION ! ne pas mettre de fichiers avec des accents dans leur nom', {'fields': [('photo', 'livret'),]}),
        ("Parent : choisir l'oeuvre finale liée aux esquisses", {'fields': ['parent']}),
    ]


    list_display = ('titre','periode','photo','livret','ordre','parent')

    list_filter = ['categorie','periode']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = Oeuvre.objects.filter(parent__id=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Oeuvre, OeuvreAdmin)
admin.site.register(Categorie)
admin.site.register(Theme)


