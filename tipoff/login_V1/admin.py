from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import IPBlock

admin.site.register(IPBlock)

# from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

# @admin.register(CustomUser)
# class User(admin.ModelAdmin):
# 	list_display = ["email","full_name"]
# 	search_fields=('email','name')
	# list_filter= ['material_shape']

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ('email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password','first_name','last_name','DOB')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
# admin.site.register(CustomUser, CustomUserAdmin)