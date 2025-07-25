from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Produto

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index (request):
    produtos = Produto.objects.all()
    
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato (request):
   
    return render(request, 'contato.html')

def produto (request, id):
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)
