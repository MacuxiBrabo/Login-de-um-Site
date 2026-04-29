from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'cadastro/index_cadastro.html', {
                'erro': 'Preencha todos os campos'
            })

        adiciona_usuario = User.objects.create_user(
            username = username,
            password = password
        )

        return redirect('login')

    return render(request, 'cadastro/index_cadastro.html')
