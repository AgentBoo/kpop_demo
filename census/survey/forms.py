from django import forms 
from .models import Survey 
from census.choices import countries 

AGE_CHOICES = [('0-12','younger than 13'), ('13-17','13-17'), ('18-24','18-24'), ('25-34', '25-34'), ('35-44','35-44'), ('45-54','45-54'), ('55-64','55-64'), ('65-200','65+')]
COUNTRY_CHOICES = [ (country,country) for country in countries ]  
ARTIST_CHOICES = [('Lee Taemin', 'Lee Taemin'), ('Kim Taeyeon','Kim Taeyeon'), ('Kim Tae-hyung', 'Kim Tae-hyung (V)')]

class SurveyForm(forms.ModelForm):
	age = forms.ChoiceField(choices=AGE_CHOICES, widget=forms.Select(attrs={ 
		'class':'selectpicker form-control',
		'title': 'Choose one of the following...'
		}))
	
	country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select(attrs={ 
		'class':'selectpicker form-control', 
		'data-live-search':'true',
		'title':'Choose one of the following...'
		}))

	artist = forms.ChoiceField(choices=ARTIST_CHOICES, widget=forms.Select(attrs={
		'class':'selectpicker form-control', 
		'data-live-search':'true',
		'title':'Choose one of the following...'
		}))
	
	class Meta():
		model = Survey 
		fields = ('age', 'country', 'artist')