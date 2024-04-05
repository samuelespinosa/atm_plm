from django.db import models

class Customer(models.Model):
    name = models.CharField('Nombre', max_length=30)
    city = models.CharField('Ciudad', max_length=50)
    email = models.EmailField('Correo',unique=True)
    country = models.CharField('País', max_length=100)  

class Developer(models.Model):
    name = models.CharField('Nombre', max_length=30)
    last_name = models.CharField('Apellidos', max_length=60)
    cc = models.CharField('Cédula', max_length=20,unique=True)  
    process= models.ManyToManyField('Process', through='ProcessAssignment', related_name='developers')  

class Process(models.Model):
    STATE_CHOICES = (
        ('planning', 'Planeando'),
        ('developing', 'En Desarrollo'),
        ('maintaining', 'En mantenimiento'),
        ('finished', 'Finalizado'),
        ('abandoned', 'Abandonado'),
    )

    date_in = models.DateTimeField("Fecha de entrada")  
    date_out = models.DateTimeField("Fecha de finalización",blank=True)  
    date_start = models.DateTimeField("Fecha de inicio")  
    state = models.CharField('Estado', max_length=11, choices=STATE_CHOICES, default='planning')
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    developer = models.ManyToManyField('Developer', related_name='assigned_processes')
    class Meta:
        verbose_name = "Process"  # Optional, but useful for singular display
        verbose_name_plural = "Processes"  # Ensures plural form is shown in the admin

class Bill(models.Model):
    STATE_CHOICES = (
        ('estimating', 'Estimando'),
        ('paid', 'Pagado'),
        ('partially_paid', 'Parcialmente Pagado'),
        ('not_paid', 'Sin pagar'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    state = models.CharField(max_length=14, choices=STATE_CHOICES, default='estimating')


class ProcessAssignment(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

