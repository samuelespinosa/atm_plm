from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
    pass

class UserProfile(models.Model):
    TYPE_CHOICES = ( 
        ('developer', 'Developer'),
        ('customer', 'Customer'),
        ('marketing', 'marketing'),
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    type_of_user = models.CharField(max_length=10,choices=TYPE_CHOICES)

class Customer(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    city = models.CharField( max_length=50)
    phone = models.CharField(max_length=20)  
    country = models.CharField(max_length=100)  
    def clean(self):
        super().clean()
        profile = self.profile
        if profile.type_of_user != 'customer':
            raise ValidationError({'profile': 'Customer can only be created for Customer user types.'})
        if profile.user.is_superuser:
            raise  ValidationError({'profile': 'A Customer can not be a super user'})
class Employee(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE) 
    id_number = models.CharField( max_length=20,unique=True)  
    process= models.ManyToManyField('Process', through='ProcessAssignment', related_name='developers')
    def clean(self):
        super().clean()
        profile = self.profile
        if profile.type_of_user not in ('developer', 'marketing'):
            raise ValidationError({'profile': 'Employees can only be created for Developer or Marketing user types.'})

class Process(models.Model):
    STATE_CHOICES = (
        ('planning', 'Planning'),
        ('developing', 'Developing'),
        ('maintaining', 'Maintaining'),
        ('finished', 'Finished'),
        ('abandoned', 'Abandoned'),
    )

    date_in = models.DateTimeField()  
    date_out = models.DateTimeField(blank=True)  
    date_start = models.DateTimeField()  
    state = models.CharField( max_length=11, choices=STATE_CHOICES, default='planning')
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    developer = models.ManyToManyField(Employee,related_name='assigned_processes')
    class Meta:
        verbose_name = "Process"  # Optional, but useful for singular display
        verbose_name_plural = "Processes"  # Ensures plural form is shown in the admin

class Bill(models.Model):
    STATE_CHOICES = (
        ('estimating','Estimating' ),
        ('paid', 'Paid'),
        ('partially_paid', 'Partially_paid'),
        ('not_paid', 'Not paid'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    state = models.CharField(max_length=14, choices=STATE_CHOICES, default='estimating')


class ProcessAssignment(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    developer = models.ForeignKey(Employee, on_delete=models.CASCADE)

