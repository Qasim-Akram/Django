from django.urls import path
from . import views

urlpatterns =[
    path('hello',views.view_hello_world,name='view_hello_world'),
    path('',views.view_first,name="first"),
    path('viewhtml/',views.view_html,name="basic_html"),
    path('hello/<str:name>',views.hello_name,name="hello_p"),
    path('query/',views.query_check,name="query_check"),
    path('special/',views.redirct_view,name="special"),
    path('send/',views.send_info,name="sendinfo"),
    path('submit',views.submit_info,name="submit"),
    path('submitdjango',views.submit_django_foam,name="submit_django"),
    path('templete',views.templete_view,name="templete")
]