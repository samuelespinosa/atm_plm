
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name= models.CharField(max_length=100)
    city = models.CharField( max_length=50)
    phone = models.CharField(max_length=20)  
    country = models.CharField(max_length=100)  
    class Meta:
        verbose_name = "Customer"  # Optional, but useful for singular display
        verbose_name_plural = "Customers"  # Ensures plural form is shown in the admin
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES= (
        ('developer', 'Desarrollador'),
        ('marketing', 'Marketing'),
    )
    role= models.CharField(max_length=13, null=True, choices=ROLE_CHOICES, blank=True)
    id_number = models.CharField( max_length=20,unique=True)  
    process= models.ManyToManyField('Process', through='ProcessAssignment', related_name='developers')
    class Meta:
        verbose_name = "Employee"  
        verbose_name_plural = "Employees"  
class Process(models.Model):
    STATE_CHOICES = (
        ('planning', 'Planning'),
        ('developing', 'Developing'),
        ('maintaining', 'Maintaining'),
        ('finished', 'Finished'),
        ('abandoned', 'Abandoned'),
    )
    name= models.CharField(max_length=100)
    person_in_charge= models.CharField(max_length=100)
    date_in = models.DateTimeField(auto_now_add=True)
    date_out = models.DateTimeField(blank=True,null=True)  
    date_start = models.DateTimeField(blank=True)  
    status = models.CharField( max_length=11, choices=STATE_CHOICES, default='planning')
    bill = models.OneToOneField('Bill', on_delete=models.CASCADE,blank=True)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    developer = models.ManyToManyField(Employee,related_name='assigned_processes')
    class Meta:
        verbose_name = "Process"  
        verbose_name_plural = "Processes"   

class Bill(models.Model):
    STATE_CHOICES = (
        ('estimating','Estimating' ),
        ('paid', 'Paid'),
        ('partially_paid', 'Partially_paid'),
        ('not_paid', 'Not paid'),
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    state = models.CharField(max_length=14, choices=STATE_CHOICES, default='estimating')

class ProcessAssignment(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    developer = models.ForeignKey(Employee, on_delete=models.CASCADE)

