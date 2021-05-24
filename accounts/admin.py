from django.contrib import admin

from .models import Projet, Piece, Demande, Fournisseur, Fabricant, Employé, Commande

admin.site.register(Projet)
admin.site.register(Piece)
admin.site.register(Demande)
admin.site.register(Fournisseur)
admin.site.register(Fabricant)
admin.site.register(Employé)
admin.site.register(Commande)
#admin.site.register(Tag)