import os
import django
from faker import Faker
import random
from django.conf import settings 

from django.contrib.auth.models import User
from core_api.models import Customer, Employee, Process, Bill, ProcessAssignment

fake = Faker()

# Generate mock data for User, Customer, and Employee models
def generate_users_and_profiles(num_users):
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        # Create a User instance
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        # Create a Customer instance linked to the User
        customer = Customer.objects.create(
            user=user,
            company_name=fake.company(),
            city=fake.city(),
            phone=fake.phone_number(),
            country=fake.country()
        )

        # Create an Employee instance linked to the User
        employee = Employee.objects.create(
            user=user,
            role=random.choice(['developer', 'marketing']),
            id_number=fake.unique.random_number(digits=8),
        )

# Generate mock data for Process and Bill models
def generate_processes_and_bills(num_processes):
    customers = Customer.objects.all()
    employees = Employee.objects.filter(role='developer')

    for _ in range(num_processes):
        customer = random.choice(customers)
        developer = random.choice(employees)

        process = Process.objects.create(
            name=fake.bs(),
            person_in_charge=fake.name(),
            date_start=fake.future_date(),
            status=random.choice(['planning', 'developing', 'maintaining', 'finished', 'abandoned']),
            customer=customer
        )

        bill = Bill.objects.create(
            amount=random.uniform(100, 10000),
            state=random.choice(['estimating', 'paid', 'partially_paid', 'not_paid'])
        )

        process.bill = bill
        process.developer.add(developer)

        ProcessAssignment.objects.create(process=process, developer=developer)

if __name__ == '__main__':
    # Generate 10 users, customers, and employees
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atm_plm.settings')
    django.setup()
    generate_users_and_profiles(10)

    # Generate 20 processes and bills
    generate_processes_and_bills(20)
