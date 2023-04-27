from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# from django.urls import reverse
################################################
# from .forms import UserAdminCreationForm
from .decorators import get_home_page,unauthenticated_user
# from .models import CustomUser

def logout_user(request):
	print("---------------------------------------")
	print(request.user, " -- Logged out")
	print("---------------------------------------")
	logout(request)
	return redirect('login')

# Create your views here.
@unauthenticated_user
def login_page(request):
	context = {
	}
	if request.method == 'POST':
		# email = request.POST.get('email_id')
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			print(user)
			page = get_home_page(user)
			print("Page to redirect :: ",page)
			if page:
				print("---------------------------------------")
				print(user, " -- Logged in")
				print("---------------------------------------")
				login(request, user)
				return redirect("admin_home")
			else:
				message = "Something is wrong with your account.."
				context['message'] = message
		else:
			message = "Email or Password is Incorrect."
			context['message'] = message
		print(message if message else "")
	return render(request,'login/login.html', context)

