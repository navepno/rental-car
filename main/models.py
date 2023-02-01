from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    # logo_photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    daily_rate = models.FloatField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.model


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.car


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer