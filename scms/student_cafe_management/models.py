from django.db import models

# Create your models here.

class Customers(models.Model):
	idno = models.CharField("ID Number",max_length=10, primary_key=True)
	name = models.CharField("Name", max_length=40)
	phno = models.CharField("Contact Number", max_length=10)
	email=models.EmailField("Email Address",max_length=254)

	def __str__(self):
		return self.idno

class Dues(models.Model):
	cus_id=models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="ID number")
	due=models.FloatField("Amount Due")
	
	def __str__(self):
		return str(self.cus_id)
		
class Products(models.Model):
	prod_id=models.CharField("Product ID",max_length=10, primary_key=True)
	item_name=models.CharField("Product Name",max_length=40)
	availabilty=models.IntegerField("Availability",default=0)
	price=models.FloatField("Price")

	def __str__(self):
		return self.prod_id


