from django.shortcuts import render
from django.http import Http404
# Create your views here.
import users

def handle_user_signup(request):
	if request.method != 'POST
		raise Http404

	a = User()
	a.firstname = request.POST.has_key('firstname')
	a.lastname = request.POST.has_key('lastname')
	a.email = request.POST.has_key('email')
	a.birthday = request.POST.has_key('birthday')
	a.contact_no = request.POST.has_key('contact_no')

	a.save()
 