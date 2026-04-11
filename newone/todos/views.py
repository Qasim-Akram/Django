from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_hello_world(request):
    return HttpResponse("hello to the mid exam of web engineering ")

def view_first(request):
     return HttpResponse("Hell Yeh! this is first page ")