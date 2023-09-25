from django.shortcuts import render, redirect
from .models import Tenistas, Torneios, Tabela

# Create your views here.
def home(request):
  tenistas = Tenistas.objects.all()
  torneios = Torneios.objects.all()
  tabela = Tabela.objects.all()
  
  return render(request, "home.html", context={ "tenistas": tenistas, "torneios": torneios, "tabela": tabela})


def create_tenistas(request):
  if request.method == "POST":

    Tenistas.objects.create(
      title = request.POST["title"],
      nome = request.POST["nome"],
      genero = request.POST["genero"],
      patrocinio = request.POST["patrocinio"]
    )

    return redirect("home")
  return render(request, "forms_tenista.html", context={"action": "Adicionar"})


def update_tenistas(request, id):
  tenista = Tenistas.objects.get(id = id)
  if request.method == "POST":
    
      tenista.title = request.POST["title"]
      tenista.nome = request.POST["nome"]
      tenista.genero = request.POST["genero"]
      tenista.patrocinio = request.POST["patrocinio"]
      tenista.save()

      return redirect("home")
  return render(request, "forms_tenista.html", context={"action": "Atualizar","tenista": tenista})


def delete_tenistas(request, id):
  tenista = Tenistas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      tenista.delete()

    return redirect("home")
  return render(request, "are_you_sure_tenista.html", context={"tenista": tenista})











def create_torneios(request):
  if request.method == "POST":

    Torneios.objects.create(
      title = request.POST["title"],
      nomeTorneio = request.POST["nomeTorneio"],
      nomeJogador = request.POST["nomeJogador"],
      vitorias = request.POST["vitorias"]
    )

    return redirect("home")
  return render(request, "forms_torneio.html", context={"action": "Adicionar"})


def update_torneios(request, id):
  torneio = Torneios.objects.get(id = id)
  if request.method == "POST":
    
      torneio.title = request.POST["title"]
      torneio.nomeTorneio = request.POST["nomeTorneio"]
      torneio.nomeJogador = request.POST["nomeJogador"]
      torneio.vitorias = request.POST["vitorias"]
      torneio.save()

      return redirect("home")
  return render(request, "forms_torneio.html", context={"action": "Atualizar","torneio": torneio})


def delete_torneios(request, id):
  torneio = Torneios.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      torneio.delete()

    return redirect("home")
  return render(request, "are_you_sure_torneio.html", context={"torneio": torneio})








def create_tabela(request):
  if request.method == "POST":

    Tabela.objects.create(
      nome = request.POST["nome"],
      participa = request.POST["participa"],
      vitorias = request.POST["vitorias"]
    )

    return redirect("home")
  return render(request, "forms_tabela.html", context={"action": "Adicionar"})


def update_tabela(request, id):
  tabela = Tabela.objects.get(id = id)
  if request.method == "POST":
    
      tabela.nome = request.POST["nome"]
      tabela.participa = request.POST["participa"]
      tabela.vitorias = request.POST["vitorias"]
      tabela.save()

      return redirect("home")
  return render(request, "forms_tabela.html", context={"action": "Atualizar","tabela": tabela})
  

def delete_tabela(request, id):
  tabela = Tabela.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      tabela.delete()

    return redirect("home")
  return render(request, "are_you_sure_tabela.html", context={"tabela": tabela})
