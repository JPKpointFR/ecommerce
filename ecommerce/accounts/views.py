from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, login, logout, authenticate


User = get_user_model()


def signup(request):
    if request.method == "POST":
        # Traiter le formulaire
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username):
            messages.error(request, "Ce nom d'utilisateur est indisponible")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, "Le username doit être alpha numérique")
            return redirect('signup')
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect('shop')
    return render(request, "signup.html")


def login_user(request):
    if request.method == "POST":
        # Conneter l'utilisateur
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop')
        else:
            messages.error(request, "ERREUR D'AUTHENTIFICATION")
            return redirect('signup')

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecter avec succès")
    return redirect('shop')
