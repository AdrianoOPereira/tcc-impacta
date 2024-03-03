from django.shortcuts import render,redirect
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

def update(request, id):
    vnome = request.POST.get("nome")#recebe um nome novo#
    pessoa = Pessoa.objects.get(id=id)#recuperar uma pesso do banco porque ela existe#
    pessoa.nome = vnome
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)