from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.template import RequestContext
from prawcore.exceptions import OAuthException
from rest_framework.views import APIView 
from rest_framework.response import Response
import datetime
import uuid
from .models import Survey, Respondent
from .forms import SurveyForm 

# Create your views here.

import os
import praw

if settings.DEBUG:
	from dotenv import load_dotenv, find_dotenv
	load_dotenv(find_dotenv())


def get_reddit_instance():
	return praw.Reddit(client_id=os.getenv('PRAW_CLIENT'), 
					   client_secret=os.getenv('PRAW_SECRET'), 
					   user_agent=os.getenv('PRAW_USER_AGENT'),)

def get_authorized_reddit_instance():
	return praw.Reddit(client_id=os.getenv('PRAW_CLIENT'), 
					   client_secret=os.getenv('PRAW_SECRET'), 
					   user_agent=os.getenv('PRAW_USER_AGENT'), 
					   redirect_uri=os.getenv('OAUTH_CALLBACK'))


def redirect_to_survey(request):
	auth_reddit = get_authorized_reddit_instance()
	survey_state = uuid.uuid4().hex
	access_url = auth_reddit.auth.url(['identity'], survey_state, 'temporary')
	request.session['survey_state'] = survey_state

	return redirect(access_url)


def pre_survey(request):
	return render(request, 'survey/pre_survey.html')


def auth_survey(request):
	if request.method == 'GET':
		try:
			state, error, code = [ request.GET.get(param, None) for param in ('state','error','code') if request.GET ]

			if state == request.session['survey_state']:
				if error and error == 'access_denied':
					del request.session['survey_state']
					info = 'Please allow our app to access your username and cake day to continue with the survey' 
					messages.info(request, info)
					return redirect('survey:pre_survey')
			
				elif code:
					reddit = get_authorized_reddit_instance()
					reddit.auth.authorize(code)
					redditor = str(reddit.user.me())

					try:
						respondent = Respondent.objects.get(username=redditor)
						request.session['redditor'] = redditor
						info = 'You can only take this survey once'
						messages.info(request,info)
						return redirect('survey:pre_survey')

					except Respondent.DoesNotExist:
						request.session['redditor'] = redditor
						request.session.set_expiry(60*60*24)
						return redirect('survey:survey_form')
				else:
					del request.session['survey_state']
					err = 'Something went wrong. Please try again or contact our mods at r/kpop' 
					messages.error(request, err)
					return redirect('survey:pre_survey')

			else:
				del request.session['survey_state']
				err = 'Something went wrong. Please try again or contact our mods at r/kpop' 
				messages.error(request, err)
				return redirect('survey:pre_survey')

		except (ValueError, KeyError, OAuthException):
			request.session.flush()
			info = 'Something went wrong. Please try using the link to the survey again or contant our mods at r/kpop' 
			messages.info(request, info)
			return redirect('survey:pre_survey')
 

def survey_form(request):
	try:
		redditor, state = request.session['redditor'], request.session['survey_state']
		
		if redditor and state:
			if request.method == 'POST':
				form = SurveyForm(request.POST)

				if form.is_valid():
					reddit = get_reddit_instance()
					cake_day = datetime.date.fromtimestamp(reddit.redditor(redditor).created_utc)

					if cake_day < datetime.date.today():
						respondent = Respondent.objects.create(username=redditor, authentic=True)
					else: 
						respondent = Respondent.objects.create(username=redditor)

					survey = form.save(commit=False)
					survey.respondent = respondent 
					survey.save()
					return HttpResponseRedirect(reverse_lazy('survey:post_survey'))
				else:
					return render(request, 'survey/survey_form.html', {'form': form })

			if request.method == 'GET':
				try:
					Survey.objects.get(respondent__username=redditor)
					survey = Survey.objects.filter(respondent__username=redditor).values()[0]
					form = SurveyForm(initial=survey)
					return render(request, 'survey/survey_form.html', { 'form': form, 'review': True }) 

				except Survey.DoesNotExist:
					form = SurveyForm()
					return render(request, 'survey/survey_form.html', {'form': form })

	except KeyError:
		return redirect('survey:survey_redirect')


def post_survey(request):
	try:
		if request.session['redditor']:
			context = { 'redditor': request.session['redditor'] }
			return render(request, 'survey/post_survey.html', context)	
	
	except KeyError:
		request.session.flush()
		return render(request, 'survey/post_survey.html')

def results(request):
	return render(request, 'survey/results.html')

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		context = {
			'default': [
					Survey.objects.filter(age='0-12').count(), 
					Survey.objects.filter(age='13-17').count(),
					Survey.objects.filter(age='18-24').count(),
					Survey.objects.filter(age='25-34').count(),
					Survey.objects.filter(age='35-44').count(),
					Survey.objects.filter(age='45-54').count(),
					Survey.objects.filter(age='55-64').count(),
					Survey.objects.filter(age='65-200').count(),

					]
				,
			'labels': [
					'<13', 
					'13-17',
					'18-24',
					'25-34',
					'35-44',
					'45-54',
					'55-64',
					'65+'
				]
			,
			'respondents': Respondent.objects.all().count()

		}
		print(context)
		return Response(context)