from django.http import HttpResponse
from django.shortcuts import render


# def main(request):
#     return HttpResponse("This is main page")

def index(request):
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("This is about page")
    return render(request,"about.html")

def contact(request):
    # return HttpResponse("This is contact page")
    return render(request,"contact.html")

def services(request):
    # return HttpResponse("This is services page")
    return render(request,"services.html")