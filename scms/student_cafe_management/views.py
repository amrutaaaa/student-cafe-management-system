from django.shortcuts import render



def index(request):
    return render(request, 'student_cafe_management/index.html')

# Create your views here.
