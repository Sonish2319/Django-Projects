from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path("", views.main),
    path("",views.index),
    path("about",views.about),
    path("contact",views.contact),
    path("services",views.services),
]
