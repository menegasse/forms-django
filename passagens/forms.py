from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from re import search as regexSearch
from .models import Passagem, Pessoa, ClasseViagem 

class PassagemForms(forms.ModelForm):

    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida':'Data de ida', 
            'data_volta':'Data de volta', 
            'informacoes': 'Informações', 
            'classe_viagem':'Classe da Viagem'
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }
    
    
    

    def verifica_se_tem_digito(self, value:str) -> bool:
        '''Verifica se umas string contem caracteres do tipo digito'''
        return bool(regexSearch(r"\d", str(value)))

    def clean(self):
        '''Função de validação do formulário de passagem'''

        origem =  self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        
        lista_de_erro = {}

        if self.verifica_se_tem_digito(origem):
            lista_de_erro['origem'] = 'Origem não pode conter números'
        
        if self.verifica_se_tem_digito(destino):
            lista_de_erro['destino'] = 'Destion não pode conter números'
        
        if origem == destino:
            lista_de_erro['destino'] = 'Destion igual a Origem'
        
        if data_ida > data_volta:
            lista_de_erro['data_volta'] = 'O campo Data de volta precisa ser após a Data de ida'
    
        if data_ida < data_pesquisa:
            lista_de_erro['data_ida'] = 'O campo Data de ida precisa ser uma data futura'

        if lista_de_erro is not None:
            for campo, messagem in lista_de_erro.items():
                self.add_error(campo, messagem)

        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['email'] # retoar os campos do modelo selecionados
        #exclude = ['nome'] # retorna todos os campos do modelo menos os selecionados
