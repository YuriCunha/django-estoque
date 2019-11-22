from django.shortcuts import render, redirect
from .models import NotasEntradas
from .forms import FormNotasEntradas

def notaEntradaList(request):
    nota_entrada = NotasEntradas.objects.all()
    template_name = 'notaEntradaList.html'
    context = {
        'nota_entrada': nota_entrada,
    }
    return render(request, template_name, context)

def notaEntradaNew(request):
    if request.method == 'POST':
        form = FormNotasEntradas(request.POST)
        if form.is_valid:
            form.save(commit=False)
            #P.quantidade = P.quantidade + nE.quantidade

            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade + form.cleaned_data['quantidade']
            
            form.cleaned_data['produto'].preco = form.cleaned_data['preco']

            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('notaEntrada:notaEntradaList')
    else:
        form = FormNotasEntradas()
    template_name = 'notaEntradaNew.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)