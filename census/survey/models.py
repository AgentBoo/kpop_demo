from django.db import models
from census.choices import countries 

# Create your models here.
AGE_CHOICES = [('0-12','younger than 13'), ('13-17','13-17'), ('18-24','18-24'), ('25-34', '25-34'), ('35-44','35-44'), ('45-54','45-54'), ('55-64','55-64'), ('65-200','65+')]
COUNTRY_CHOICES = [ (country, country) for country in countries ] 
ARTIST_CHOICES = [('Lee Taemin', 'Lee Taemin'), ('Kim Taeyeon','Kim Taeyeon'), ('Kim Tae-hyung', 'Kim Tae-hyung (V)')]


class Respondent(models.Model):
	username = models.CharField(max_length=256, blank=True, null=True)
	authentic = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return '[%s]  username: %s  authentic: %s' % (self.id, self.username, self.authentic)


class Survey(models.Model):
	age = models.CharField(max_length=20, default='', choices=AGE_CHOICES)
	country = models.CharField(max_length=256, default='', choices=COUNTRY_CHOICES)
	artist = models.CharField(max_length=256, default='', choices=ARTIST_CHOICES) 

	respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE, related_name='survey', null=True)

	def __str__(self):
		return '[%s]  age: %s  country: %s' % (self.id, self.age, self.country)