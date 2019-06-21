from django.urls import path
from book1 import views


app_name='book1'
urlpatterns=[
    path('', views.book1, name='book1'),
    
    ]