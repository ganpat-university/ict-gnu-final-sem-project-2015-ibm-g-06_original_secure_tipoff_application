from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from login_V1.decorators import block_ips
# Create your views here.

@block_ips
def home_page(request):
	return render(request,"home/homepage.html",{})


def about_us_function(request):
	return render(request,"about_us/about_us.html",{})

def something(request):
	return render(request,"something/something.html",{})


def report(request):
	return render(request,"report/report.html",{})
	
def report_person(request):
	if request.method == 'POST':
		# if person_report_id: # if edit
		# 	form = person_report_form(request.POST, instance=edit) 
		# else: # if create
		print ("here");
		form = person_report_form(request.POST)
		if form.is_valid():
			candidate = form.save(commit=False)
			candidate.save()
			print("saved :: ", candidate)
			return redirect('home_page')
		else:
			print ("error",form.errors)
			context['errors'] = form.errors.as_ul()	

	return render(request,"report/report_person.html",{})

def report_activity(request):
		
		if request.method == 'POST':

		# if person_report_id: # if edit
		# 	form = person_report_form(request.POST, instance=edit) 
		# else: # if create
			form = activity_report_form(request.POST)
			if form.is_valid():
				candidate = form.save(commit=False)
				candidate.save()
				print("saved :: ", candidate)
				return redirect('home_page')
			else:
				context['errors'] = form.errors.as_ul()	

		return render(request,"report/report_activity.html",{})


def admin_home(request):
	my_person_reports = person_report.objects.all().filter(
		invistigated=False
	)
	my_activity_reports = activity_report.objects.all().filter(
		invistigated=False
	)
	print("asdasd")
	context = {
		"my_person_reports":my_person_reports,
		"my_activity_reports":my_activity_reports,
	}
	return render(request,"admin/home.html",context)

def show_activity_report(request):
	show_activity_report = activity_report.objects.all().filter(invistigated=False)
	context = {
		"result":show_activity_report
		
	}
	return render(request,"admin/show_activity_report.html",context)
def show_person_report(request):
	show_person_report = person_report.objects.all().filter(invistigated=False)
	context = {
		"result":show_person_report
		
	}
	return render(request,"admin/show_person_report.html",context)

def show_wnatedlist(request):
	show_wnatedlist = wanted_list.objects.all()
	context = {
		"result":show_wnatedlist
		
	}
	return render(request,"admin/show_wantedlist.html",context)

def show_investigated_report(request):
	show_investigated_report = activity_report.objects.all().filter(invistigated=True)
	print(show_investigated_report)
	context = {
		"result":show_investigated_report
		
	}
	return render(request,"admin/investigated_report.html",context)