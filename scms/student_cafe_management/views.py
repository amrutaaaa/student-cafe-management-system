from django.shortcuts import *
from django.views import *
from .models import *

# class ProductsView(generic.lView):
    
def index(request):
    return render(request, 'student_cafe_management/index.html')

def dues(request):
    return render(request, 'student_cafe_management/dues.html')


    
def products(request):
    products_list=Products.objects.all()
    print(products_list)
    item_name=[]
    quant=[]
    price=[]
    pk=[]
    xl=[]
    # context['product_list'] = Products.objects.all()
    for p in products_list:
        pk.append(p)
        print(p)
        x=Products.objects.get(pk=p)
        print(x)
        # print(x.pk)
        xl.append(x)
        # item_name.append(x.item_name)
        # quant.append(x.availabilty)
        # price.append(x.price)
        # print(price,prod_name)
    # # a="kl"
    # context={'item_name':item_name,'pk':pk,'quant':quant,'price':price}
    context={ 'product_list': xl}

    
    return render(request, 'student_cafe_management/products.html',context)

def newbill(request):
    return render(request, 'student_cafe_management/newbill.html')

# Create your views here.
