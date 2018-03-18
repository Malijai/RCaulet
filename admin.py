from django.contrib import admin

from .models import Categorie, Oeuvre, Theme


class OeuvreAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informations', {'fields': ['titre','periode', 'texte','dimension',]}),
        ('Classification', {'fields': [('categorie', 'theme', 'ordre'),]}),
        ('Fichiers', {'fields': [('photo', 'livret'),]}),
        ('Parent', {'fields': ['parent']}),
    ]


    list_display = ('titre','periode')

    list_filter = ['categorie','periode']


    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Oeuvre, OeuvreAdmin)
admin.site.register(Categorie)
admin.site.register(Theme)

