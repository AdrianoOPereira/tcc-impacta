from django.shortcuts import render
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    vnome = request.POST.get("nome")
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)#pegar o usuario do banco de dados#
    return render(request, "update.html", {"pessoa": pessoa})#enjetei a variavel pessoa no template#