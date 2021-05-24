from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Demande, Projet, Piece, Fournisseur, Employé, Commande, Piece
from .forms import DemandeForm, FournisseurForm, CreateUserForm, EmployéForm, CommandeForm, PieceForm
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username ou Password est invalide')

    context = {}
    return render(request, 'accounts/login.html', context)

@login_required(login_url='loginPage')
def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='loginPage')
def home(request):
    demandes = Demande.objects.all().order_by('-date_creation')
    projets = Projet.objects.all().order_by('-date_creation')
    fournisseurs = Fournisseur.objects.all().order_by('-date_creation')
    total_demandes = demandes.count()
    demandes_validees = demandes.filter(statut='Validée').count()
    non_validees = demandes.filter(statut='Non Validée').count()
    context = {'demandes':demandes, 'projets':projets, 'fournisseurs': fournisseurs, 'total_demandes':total_demandes, 'demandes_validees':demandes_validees, 'non_validees':non_validees}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['magasinier'])
def pieces(request):
    pieces = Piece.objects.all().order_by('-date_creation')
    return render(request, 'accounts/pieces.html', {'pieces': pieces})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['magasinier'])
def ajouter_piece(request):
    form = PieceForm()
    if request.method == 'POST':
        form = PieceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'pièce ajoutée avec succès')
            return redirect('/ajouter_piece/')
    context = {'form': form}
    return render(request, 'accounts/pieceform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['magasinier'])
def modifier_piece(request, piece_id):
    piece = Piece.objects.get(id=piece_id)
    form = PieceForm(instance=piece)
    if request.method == 'POST':
        form = PieceForm(request.POST, instance=piece)
        if form.is_valid():
            form.save()
            return redirect('/pieces/')   
    context = {'form': form}
    return render(request, 'accounts/pieceform.html', context)
7
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['magasinier'])
def supprimer_piece(request, piece_id):
    piece = Piece.objects.get(id=piece_id)
    if request.method == 'POST':
        piece.delete()
        return redirect('/pieces/')  
    context = {'item': piece }
    return render(request, 'accounts/deletepiece.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def employés(request):
    employés = Employé.objects.all().order_by('-date_creation')
    return render(request, 'accounts/employés.html', {'employés': employés})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def creer_compte(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'session ajoutée avec succès')
            return redirect('creer_compte')
    context = {'form': form}
    return render(request, 'accounts/session.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def creer_employé(request):
    form = EmployéForm()
    if request.method == 'POST':
        form = EmployéForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'employé ajouté avec succès')
            return redirect('creer_employé')
    context = {'form': form}
    return render(request, 'accounts/employéform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def modifier_employé(request, employé_id):
    employé = Employé.objects.get(id=employé_id)
    form = EmployéForm(instance=employé)
    if request.method == 'POST':
        form = EmployéForm(request.POST, instance=employé)
        if form.is_valid():
            form.save()
            return redirect('/employés/')   
    context = {'form': form}
    return render(request, 'accounts/employéform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def supprimer_employé(request, employé_id):
    employé = Employé.objects.get(id=employé_id)
    if request.method == 'POST':
        employé.delete()
        return redirect('/employés/')  
    context = {'item': employé }
    return render(request, 'accounts/deleteemp.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    demandes = fournisseur.demande_set.all().order_by('-date_creation')
    total_demandes = demandes.count()
    
    '''if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        
        send_mail(
            message_name, # subject
            message,
            message_email, # from email
            [wessimzeckri1999@gmail.com], # to email
        )'''

    return render(request, 'accounts/fournisseur.html', {'fournisseur':fournisseur, 'demandes': demandes, 'total_demandes':total_demandes})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def fournisseurs(request):
    fournisseurs = Fournisseur.objects.all().order_by('-date_creation')
    return render(request, 'accounts/fournisseurs.html', {'fournisseurs': fournisseurs})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def creer_fournisseur(request):
    form = FournisseurForm()
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fournisseurs/')
    context = {'form': form}
    return render(request, 'accounts/fournisseurform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def modifier_fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    form = FournisseurForm(instance=fournisseur)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('/fournisseurs/')   
    context = {'form': form}
    return render(request, 'accounts/fournisseurform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def supprimer_fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('/fournisseurs/')  
    context = {'item': fournisseur }
    return render(request, 'accounts/deletefourn.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def demval(request):
    demandes = Demande.objects.all()
    demandes_validees = demandes.filter(statut='Validée').order_by('-date_creation')
    return render(request, 'accounts/demval.html', {'demandes' : demandes,'demandes_validees': demandes_validees})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def lancer_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'commande ajoutée avec succès')
            return redirect('/lancer_commande/')
    context = {'form': form}
    return render(request, 'accounts/commandeform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'accounts/commandes.html', {'commandes' : commandes})

@login_required(login_url='loginPage')
def projet(request, projet_id):
    projet = Projet.objects.get(id=projet_id)
    demandes = projet.demande_set.all().order_by('-date_creation')
    total_demandes = demandes.count()
    return render(request, 'accounts/projet.html', {'projet':projet, 'demandes': demandes, 'total_demandes':total_demandes})

@login_required(login_url='loginPage')
def projets(request):
    projets = Projet.objects.all().order_by('-date_creation')
    return render(request, 'accounts/projets.html', {'projets': projets})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['chef projet'])
def demandes(request):
    demandes = Demande.objects.all().order_by('-date_creation')
    demandes_validees = demandes.filter(statut='Validée')
    non_validees = demandes.filter(statut='Non Validée')
    return render(request, 'accounts/demandes.html', {'demandes':demandes, 'demandes_validees':demandes_validees, 'non_validees':non_validees})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['direction'])
def demdir(request):
    demandes = Demande.objects.all().order_by('-date_creation')
    demandes_validees = demandes.filter(statut='Validée')
    non_validees = demandes.filter(statut='Non Validée')
    return render(request, 'accounts/demdir.html', {'demandes':demandes, 'demandes_validees':demandes_validees, 'non_validees':non_validees})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['direction'])
def success(request):
    return render(request, 'accounts/success.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['chef projet'])
def creer_demande(request):
    form = DemandeForm()
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'demande ajoutée avec succès')           
            return redirect('/creer_demande/')
    context = {'form': form}
    return render(request, 'accounts/demandeform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['chef projet','direction'])
def modifier_demande(request, demande_id):
    demande = Demande.objects.get(id=demande_id)
    form = DemandeForm(instance=demande)
    if request.method == 'POST':
        form = DemandeForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('demandes')   
    context = {'form': form}
    return render(request, 'accounts/demandeform.html', context)
7
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['chef projet'])
def supprimer_demande(request, demande_id):
    demande = Demande.objects.get(id=demande_id)
    if request.method == 'POST':
        demande.delete()
        return redirect('/')  
    context = {'item': demande }
    return render(request, 'accounts/delete.html', context)
