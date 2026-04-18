from django.shortcuts import render

# Create your views here.

def login(request):

    return render(request, 'login/index_login.html')