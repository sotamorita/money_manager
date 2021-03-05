from django.contrib import admin
from django.urls import path
from .views import signupfunc, loginfunc, indexfunc, logoutfunc, createfunc, deletefunc, updatefunc, glfunc

urlpatterns = [
    path('index/', indexfunc, name='index'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('create/', createfunc, name='create'),
    path('delete/<int:pk>/', deletefunc, name='delete'),
    path('update/<int:pk>/', updatefunc, name='update'),
    path('gl/', glfunc, name='gl'),
]
