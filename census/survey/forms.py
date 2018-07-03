from django import forms 
from .models import Survey 
from countries import countries 

COUNTRY_CHOICES = [ (country,country) for country in countries ]  
ARTIST_CHOICES = [('Lee Taemin', 'Lee Taemin'), ('Kim Taeyeon','Kim Taeyeon'), ('Kim Tae-hyung', 'Kim Tae-hyung (V)')]

class SurveyForm(forms.ModelForm):
	age = forms.IntegerField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder': ''
		}))
	country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select(attrs={
		'class':'selectpicker form-control', 
		"data-live-search":"true",
		'title':"Choose one of the following..."
		}))
	artist = forms.ChoiceField(choices=ARTIST_CHOICES, widget=forms.Select(attrs={
		'class':'selectpicker form-control', 
		"data-live-search":"true",
		'title':"Choose one of the following..."
		}))
	
	class Meta():
		model = Survey 
		fields = ('age','country','artist')