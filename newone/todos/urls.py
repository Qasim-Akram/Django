from django.urls import path
from . import views

urlpatterns =[
    path('hello',views.view_hello_world,name='view_hello_world'),
    path('',views.view_first,name="first")
]