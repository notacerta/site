from django import forms
from .models import post


class PostForm(forms.ModelForm):

	class Meta:
		model = post
		fields = ('check_empresa', 'empresa', 'check_ramo', 'ramo', 'name', 'email', 'cidade', 'estado')
		labels = {
			'check_empresa': ('Você tem uma empresa?'),
			'empresa': ('Nome:'),
			'check_ramo': ('Mas tem pretensão de abrir uma?'),
			'ramo': ('E qual seria o ramo da sua futura empresa?'),
            'name': ('Nome Completo:'),
            'email': ('E-mail:'),
        }
		widgets = {
			'check_empresa': forms.RadioSelect(attrs = {'onclick' : "yesnoCheck(\'id_check_empresa_0\');"}),
			'check_ramo': forms.RadioSelect(attrs = {'onclick' : "yesnoCheck(\'id_check_ramo_0\');"})
		}