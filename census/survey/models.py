from django.db import models
from countries import countries 

# Create your models here.

COUNTRY_CHOICES = [ (country,country) for country in countries ] 
ARTIST_CHOICES = [('Lee Taemin', 'Lee Taemin'), ('Kim Taeyeon','Kim Taeyeon'), ('Kim Tae-hyung', 'Kim Tae-hyung (V)')]


class Respondent(models.Model):
	username = models.CharField(max_length=256, blank=True, null=True)
	authentic = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return '[%s]  username: %s  authentic: %s' % (self.id, self.username, self.authentic)


class Survey(models.Model):
	age = models.IntegerField(null=True)
	country = models.CharField(max_length=256, default='', choices=COUNTRY_CHOICES)
	artist = models.CharField(max_length=256, default='', choices=ARTIST_CHOICES) 

	respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE, related_name='survey', null=True)

	def __str__(self):
		return '[%s]  age: %s  country: %s' % (self.id, self.age, self.country)