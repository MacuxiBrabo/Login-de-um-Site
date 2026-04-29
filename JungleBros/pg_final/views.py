from django.shortcuts import render

# Create your views here.

def pg_final(request):

    return render(request, 'pg_final/index_paginafinal.html', {'usuario': request.user})