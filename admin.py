from django.contrib import admin

from .models import Categorie, Oeuvre

class OeuvreAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informations', {'fields': ['titre','periode', 'texte','dimension',]}),
        ('Classification', {'fields': ['categorie', 'ordre',]}),
        ('Fichiers', {'fields': ['photo', 'livret', ]}),
    ]

    list_display = ('categorie', 'titre','periode')

    list_filter = ['categorie','periode']

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Oeuvre, OeuvreAdmin)
admin.site.register(Categorie)