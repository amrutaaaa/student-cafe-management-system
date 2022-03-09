from django.contrib import admin
from .models import Products, Customers, Dues

# Register your modelsoo here.
class ProductsAdmin(admin.ModelAdmin):
   fieldsets=[
    ('Product Information',{'fields': ['prod_id','item_name']}),
    ('Availability and Price', {'fields':['availabilty', 'price']}) ,]

admin.site.register(Products, ProductsAdmin)

class CustomersAdmin(admin.ModelAdmin):
   fieldsets=[
    ('Customer Information',{'fields': ['idno','name']}),
    ('Contact Information', {'fields':['phno', 'email']}) ,]

admin.site.register(Customers, CustomersAdmin)

admin.site.register(Dues)
