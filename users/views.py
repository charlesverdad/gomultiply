from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
# Create your views here.
from users.models import *

def handle_user_signup(request):
	if request.method != 'POST':
		raise Http404


	print request.POST

	return HttpResponse('hello world!')
 	
