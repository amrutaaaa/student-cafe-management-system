from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'student_cafe_management/index.html')

def dues(request):
    return render(request, 'student_cafe_management/dues.html')
    
def products(request):
    products_list=Products.objects.all()
    print(products_list)
    return render(request, 'student_cafe_management/products.html')

def newbill(request):
    return render(request, 'student_cafe_management/newbill.html')

# Create your views here.
