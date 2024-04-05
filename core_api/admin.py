from django.contrib import admin
from .models import Process, Developer, Bill, Customer,ProcessAssignment
admin.site.register(Process)
admin.site.register(Developer)
admin.site.register(Bill)
admin.site.register(Customer)
admin.site.register(ProcessAssignment)
# Register your models here.
