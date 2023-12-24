from django.contrib import admin
from backend_api.models import Student
# Register your models here.

class AdminModel(admin.ModelAdmin):
    list = ('name','age')
    admin.site.register(Student)