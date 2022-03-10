from django.shortcuts import *
from django.views import *
from django.utils import *
from .models import *
import datetime

def index(request):
    return render(request, 'student_cafe_management/index.html')

def dues(request):
    dues_list=Dues.objects.all()
    print(dues_list)
    global dl
    dl=[]
    
    for p in dues_list:
        x=Customers.objects.get(pk=p)
        y=x.dues_set.get()
        dl.append(y)
    
    context={'dues_list': dl}
    return render(request, 'student_cafe_management/dues.html',context)
    
global xl
    
def products(request):
    products_list=Products.objects.all()
    global xl
    xl=[]
    for p in products_list:
        x=Products.objects.get(pk=p)
        xl.append(x)
    context={ 'product_list': xl}
    return render(request, 'student_cafe_management/products.html',context)

global sum
sum=0
global bought_list
bought_list={}

def newbill(request):
    global xl,sum,bought_list
    products_list=Products.objects.all()
    xl=[]
    
    for p in products_list:
        x=Products.objects.get(pk=p)
        xl.append(x)
    context={ 'product_list': xl,"quant":0,"prod":None,'sum':0}

    if request.method == 'GET':
        sum=0
        bought_list={}
    if request.method == 'POST':
        print("form successful")
        product_id=request.POST['product']
        quant=int(request.POST['quant'])
        customer=(request.POST['stud_id'])
        x=Products.objects.get(pk=product_id)
        x.availabilty-=quant
        x.save()
        bought_list[x]=quant
        sum=sum+(quant*(x.price))
        customerob=Customers.objects.get(pk=customer)
        name= customerob.name
        
        dues=Dues.objects.get(cus_id=customer)
        dues.due+=(quant*(x.price))
        
        dues.save()
        
        context={ 'product_list': xl,'bought_list':bought_list,'sum':sum,'tot_price':quant*(x.price),'customerob': customerob}
       
    

    return render(request, 'student_cafe_management/newbill.html',context)


