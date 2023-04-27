from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(activity_report)
admin.site.register(person_report)
admin.site.register(wanted_list)


