from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pieces/', views.pieces, name="pieces"),
    path('ajouter_piece/', views.ajouter_piece, name="ajouter_piece"),
    path('modifier_piece/<int:piece_id>/', views.modifier_piece, name="modifier_piece"),
    path('supprimer_piece/<int:piece_id>/', views.supprimer_piece, name="supprimer_piece"),
    path('creer_compte/', views.creer_compte, name="creer_compte"),
    path('employés/', views.employés, name="employés"),
    path('creer_employé/', views.creer_employé, name="creer_employé"),
    path('modifier_employé/<int:employé_id>/', views.modifier_employé, name="modifier_employé"),
    path('supprimer_employé/<int:employé_id>/', views.supprimer_employé, name="supprimer_employé"),
    path('fournisseur/<int:fournisseur_id>', views.fournisseur, name="fournisseur"),
    path('fournisseurs/', views.fournisseurs, name="fournisseurs"),
    path('creer_fournisseur/', views.creer_fournisseur, name="creer_fournisseur"),
    path('modifier_fournisseur/<int:fournisseur_id>/', views.modifier_fournisseur, name="modifier_fournisseur"),
    path('supprimer_fournisseur/<int:fournisseur_id>/', views.supprimer_fournisseur, name="supprimer_fournisseur"),
    path('projet/<int:projet_id>/', views.projet, name="projet"),
    path('projets/', views.projets, name="projets"),
    path('demandes/', views.demandes, name="demandes"),    
    path('creer_demande/', views.creer_demande, name="creer_demande"),
    path('modifier_demande/<int:demande_id>/', views.modifier_demande, name="modifier_demande"),
    path('supprimer_demande/<int:demande_id>/', views.supprimer_demande, name="supprimer_demande"),
    path('demval/', views.demval, name="demval"),
    path('demdir/', views.demdir, name="demdir"), 
    path('success/', views.success, name="success"), 
    path('lancer_commande/', views.lancer_commande, name="lancer_commande"),
    path('commandes/', views.commandes, name="commandes"),        
    path('login', views.loginPage, name="loginPage"),
    path('logout', views.logoutUser, name="logoutUser"),
    path('user', views.userPage, name="userPage"),
]
