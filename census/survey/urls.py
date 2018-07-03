from django.urls import path
from . import views 


app_name = 'survey'

urlpatterns = [
	path('', views.redirect_to_survey, name='survey_redirect'),
	path('pre', views.pre_survey, name='pre_survey'),
	path('auth', views.auth_survey, name='survey_auth'),
	path('form', views.survey_form, name='survey_form'),
	path('thanks', views.post_survey, name='post_survey'),
	path('results', views.results, name='results'),
]