from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from .forms import PersonForm
# Create your views here.
def view_hello_world(request):
    return HttpResponse("hello to the mid exam of web engineering ")

def view_first(request):
     return HttpResponse("Hell Yeh! this is first page ")

def view_html(request):
     return render(request,"todos/index.html ")

def hello_name(request,name):
     return HttpResponse(f'hello!{name}')

def query_check(request):
     return HttpResponse(f'Your query was :{request.GET.get("q") }')

def redirct_view(request):
     return redirect('basic_html')

def send_info(request):
     if request.method == 'POST':
         form = PersonForm(request.POST)

         if form.is_valid():
          name = form.cleaned_data['name']
          age = form.cleaned_data['age']
          job = form.cleaned_data['job']
          return HttpResponse(f'You submit {name},{age},{job}')
     else:
          return HttpResponseNotAllowed(['POST'])

    
def submit_info(request):
     return render(request,'todos/submit_detail.html')

def submit_django_foam(request):
    foam = PersonForm()
    return render(request,'todos/submit_django.html',{'foam':foam})

def templete_view(request):
    context ={ 
        "name":"Qasim Akram",
        "Age":21,
        "speciality":["python","sql"]
    }
    return render(request,'todos/templete_demo.html',context)