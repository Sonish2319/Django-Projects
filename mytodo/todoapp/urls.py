from django.shortcuts import render, HttpResponse
from django.urls import path
from todoapp import views

urlpatterns = [
    path("",views.signup, name="signup"),
    path("login",views.login_view, name="login"),
    path("todo",views.todo,name="todo"),
    path('signout',views.signout,name="signout"),
]
