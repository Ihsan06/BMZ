from django.contrib import admin

# Register your models here.

from .models import User, Country, Project

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Project)
