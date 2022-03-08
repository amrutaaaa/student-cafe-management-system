from django.shortcuts import render



def index(request):
    return render(request, 'student_cafe_management/index.html')

def dues(request):
    return render(request, 'student_cafe_management/dues.html')
    
def products(request):
    return render(request, 'student_cafe_management/products.html')

def newbill(request):
    return render(request, 'student_cafe_management/newbill.html')

# Create your views here.
