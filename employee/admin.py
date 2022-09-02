from django.contrib import admin

from employee.models import department, employee, role

# Register your models here.

admin.site.register(department)
admin.site.register(role)
admin.site.register(employee)