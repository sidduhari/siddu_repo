from django.contrib import admin

# Register your models here.
from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone_number']
admin.site.register(Employee,EmployeeAdmin)