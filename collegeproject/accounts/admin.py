from django.contrib import admin

# Register your models here.
from accounts.models import Course, Department, Person

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Person)