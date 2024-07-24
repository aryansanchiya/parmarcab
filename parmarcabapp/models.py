from django.db import models

# Create your models here.
class CabsOnlineForm(models.Model):
    customer_name = models.CharField(max_length=250)
    customer_email = models.EmailField()
    mo_no = models.IntegerField()
    cab_type = models.CharField(max_length=100)
    from_destination = models.CharField(max_length=200)
    to_destination = models.CharField(max_length=200)
    journey_date = models.CharField(max_length=50)
    journey_time = models.TimeField()
    datetime = models.DateField(auto_now_add=True)

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.state}"

class Trips(models.Model):
    name = models.CharField(max_length=250)
    # price = models.IntegerField()
    offer = models.CharField(max_length=250,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    sedan = models.IntegerField(null=True)
    suv = models.IntegerField(null=True)
    hatchback = models.IntegerField(null=True)
    xuv = models.IntegerField(null=True)
    luxury = models.IntegerField(null=True)