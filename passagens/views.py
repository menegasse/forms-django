from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms

def index(request):
    context = {
                'form_passagem': PassagemForms(), 
                'form_pessoa': PessoaForms()
            }
    return render(request, 'index.html', context)

def minha_consulta(request):
    if request.method == 'POST':
        context = {
                'form_passagem': PassagemForms(request.POST), 
                'form_pessoa': PessoaForms(request.POST)
        }
        render_page =  'minha_consulta.html' if context['form_passagem'].is_valid() else 'index.html'
        return render(request, render_page , context)