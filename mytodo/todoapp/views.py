from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todoapp import models
from todoapp.models import TODO
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        emailid = request.POST.get("emailid")
        pwd = request.POST.get("pwd")

        print(fnm,emailid,pwd)

        my_user = User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        
        return redirect('/login')
  




    return render(request,'sign.html')


def login_view(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')

        userr = authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr) # login this is import 
            return redirect('/todo')
        else:
            return redirect('/login')


        print(fnm,pwd)

    return render(request,'login.html')

def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODO(title=title, user=request.user)
        obj.save()
        # Fetch todos ordered by date for the current user
        res = models.TODO.objects.filter(user=request.user).order_by('-date')
        return render(request, 'todo.html', {'res': res})

    # Fetch todos ordered by date for the current user in GET request
    res = models.TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})


def signout(request):
    logout(request)
    return redirect('login')