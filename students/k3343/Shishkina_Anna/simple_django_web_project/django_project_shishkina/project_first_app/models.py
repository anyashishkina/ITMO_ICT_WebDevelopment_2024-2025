from django.db import models

# Create your models here.

# Автовладелец
class Owner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

class Car(models.Model):
    car_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30, null=True)

# Владение
class Ownership(models.Model):
    owner_id = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    beginning = models.DateField()
    ending = models.DateField()

# Водительское удостоверение
class License(models.Model):
    owner = models.ForeignKey(Owner, null=False, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    receiving_date = models.DateField()
