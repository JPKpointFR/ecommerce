from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()


def signup(request):
    if request.method == "POST":
        # Traiter le formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('shop')
    return render(request, "signup.html")


def login_user(request):
    if request.method == "POST":
        # Conneter l'utilisateur
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username, password)
        if user:
            login(request, user)
            return redirect('shop')

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('shop')
