from django.db import models

# Create your models here.


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=10, default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(max_length=250, default="")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
