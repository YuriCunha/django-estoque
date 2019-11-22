from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Cores

from .forms import FormCores

def index(request):
    template_name = 'index.html'

    lista = [
        {'nome': 'André', 'idade': 45},
        {'nome': 'Pedro', 'idade': 60},
        {'nome': 'João', 'idade': 70},
    ]

    context = {
        'lista': lista
    }
    return render(request, template_name, context)


def cor(request):
    cores = Cores.objects.all()
    template_name = 'cor.html'
    context = {
        'cores': cores,
    }
    return render(request, template_name, context)

def corNews(request):
    if request.method == "POST":
        form = FormCores(request.POST)
        if form.is_valid:
            form.save()
            return redirect('cor')
    else:
        form = FormCores()
        print(form)
    template_name = 'corNews.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def corDelete(request, pk):
    cor = Cores.objects.get(pk=pk)
    cor.delete()
    return redirect('cor')

def corUpdate(request, pk):
    cor = Cores.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormCores(request.POST, instance=cor)
        if form.is_valid:
            form.save()
            return redirect('cor')
    else:
        form = FormCores(instance=cor)
    template_name = 'corUpdate.html'
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, template_name, context)