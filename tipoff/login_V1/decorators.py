from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout

from .models import IPBlock
################ returns home if logged in or login if not #################

def unauthenticated_user(next_fun):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            print("logged in user found")
            page = get_home_page(request.user)
            if page:
                return redirect(page)
        else:
            return next_fun(request,*args,**kwargs)
    return wrapper_function


################ returns home page #################
def get_home_page(user):
	print("here at decorator:",user.groups.all())
	if user.groups.all():
		if str(user.groups.all()[0]) == 'admin':
			# return '/admin/'
			return 'home_page'
		elif str(user.groups.all()[0]) == 'root':
			return 'home_page'
		elif str(user.groups.all()[0]) == 'manager':
			return 'home_page'
		elif str(user.groups.all()[0]) == 'member':
			return 'home_page'
	else:
		return "home_page"

################ returns home if logged in or login if not #################
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            user_groups_set = None
            if request.user.groups.exists():
                groups = request.user.groups.all()
                user_groups_set = set()
                for group in groups:
                    user_groups_set.add(group.name)
            allowed_roles_set = set(allowed_roles)
            if user_groups_set & allowed_roles_set:
                # print(request.user,"here")
                return view_func(request,*args,**kwargs)
            else:
                logout(request)
                return redirect('login')
                # return HttpResponse("hii")
        return wrapper_func
    return decorator

################ returns True or False if the IP address is Blocked #################
import ipaddress

def is_ip_blocked(ip_address):
    blocked_ips = IPBlock.objects.filter(ip_address=ip_address)
    blocked_ranges = IPBlock.objects.filter(ip_range__isnull=False)

    for ip_block in blocked_ips:
        if ip_block.ip_address == ip_address:
            return True

    for ip_block in blocked_ranges:
        cidr_ip = ipaddress.IPv4Network(ip_block.ip_range)
        if ipaddress.IPv4Address(ip_address) in cidr_ip:
            return True
    return False

def block_ips(view_func):
    def wrapped_view(request, *args, **kwargs):
        ip_address = request.META.get('REMOTE_ADDR')
        print("IP Address :: ",ip_address)
        if is_ip_blocked(ip_address):
            return render(request, 'blocked.html')
        # blocked_ips = IPBlock.objects.filter(ip_address=ip_address)
        # blocked_ranges = IPBlock.objects.filter(ip_range__contains=ip_address)

        # if blocked_ips or blocked_ranges:
        #     return render(request, 'blocked.html')

        return view_func(request, *args, **kwargs)
    return wrapped_view