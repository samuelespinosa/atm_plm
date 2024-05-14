from django.contrib import admin
from .models import Process, Employee, Bill, Customer,ProcessAssignment

admin.site.register(Process)
admin.site.register(Employee)
admin.site.register(Bill)
admin.site.register(Customer)
admin.site.register(ProcessAssignment)

# Register your models here.
