from django.db import models

# Create your models here.

class Customers(models.Model):
	idno = models.CharField("ID Number",max_length=10, primary_key=True)
	name = models.CharField("Name", max_length=40)
	phno = models.CharField("Contact Number", max_length=10)
	email=models.EmailField("Email Address",max_length=254)

	def __str__(self):
		return self.name

class Dues(models.Model):
	cus_id=models.ForeignKey(Customers, on_delete=models.CASCADE)
	
