from django import forms
from .models import UrlShrinked

class UrlShrinkedForm(forms.ModelForm):
	
	class Meta:
		model = UrlShrinked
		fields=('url',)
	