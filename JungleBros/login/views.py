from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.

def login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        autenticar = authenticate(request, username = username, password = password)

        if autenticar is not None:
            auth_login(request, autenticar)
            return render(request, 'login/index_paginafinal.html', {'username': autenticar.username})
        else:
            messages.error(request, 'Usuário ou senha incorretos')
        

    return render(request, 'login/index_login.html')