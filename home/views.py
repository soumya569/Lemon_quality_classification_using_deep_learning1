from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("This is our home page")
    return render(request,"index.html")

def about(request):
   # return HttpResponse("This is our about page")
    return render(request,"about.html")

def contact(request):
    #return HttpResponse("This is our contact page")
    return render(request,"contact.html")
def login(request):
    #return HttpResponse("This is our contact page")
    return render(request,"login.html")

def registration(request):
    #return HttpResponse("This is our contact page")
    return render(request,"registration.html")


