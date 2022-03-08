from django.urls import path
from . import views  # . means same directory

urlpatterns=[path('', views.index, name='index'), path('dues', views.dues, name='dues'), path('newbill', views.newbill, name='newbill'),path('products', views.products, name='products'),]