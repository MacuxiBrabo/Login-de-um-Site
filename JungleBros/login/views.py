from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.

def login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        autenticar = authenticate(
            request, 
            username = username, 
            password = password
            )

        if autenticar is not None:
            auth_login(request, autenticar)
            return redirect('pagina_final')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
            return redirect('login')
        

    return render(request, 'login/index_login.html')
