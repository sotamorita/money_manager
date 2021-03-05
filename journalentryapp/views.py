import csv
import pandas as pd
import numpy as np
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import JournalentryModel
from .forms import  JournalentryForm
from .modules import modules

# Create your views here.

@login_required
def indexfunc(request):
    template_name = './journalentryapp/index.html'
    model = JournalentryModel
    object_list = model.objects.all()
    filepath = "journalentryapp/output/data.csv"
    context = modules.module_sum(filepath, object_list)
    return render(request, template_name, context)

def signupfunc(request):
    template_name = './journalentryapp/signup.html'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('index')
        except IntegrityError:
            return render(request, template_name, {'error':'このユーザーはすでに登録されています。'})
    return render(request, template_name, {})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, './journalentryapp/login.html', {})
    return render(request, './journalentryapp/login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def createfunc(request):
    template_name = './journalentryapp/create.html'
    model = JournalentryModel
    form = JournalentryForm(request.POST or None)
    context = {}
    if form.is_valid():
        form.save()
        modules.module_output(model)
        return redirect('index')
    context['form'] = form
    return render(request, template_name, context)

def deletefunc(request, pk):
    template_name = './journalentryapp/delete.html'
    context = {}
    model = JournalentryModel
    obj = get_object_or_404(JournalentryModel, pk=pk)
    if request.method == "POST":
        obj.delete()
        modules.module_output(model)
        return redirect('index')
    return render(request, template_name, context)

def updatefunc(request, pk):
    template_name = './journalentryapp/update.html'
    context = {}
    model = JournalentryModel
    obj = get_object_or_404(JournalentryModel, pk=pk)
    form = JournalentryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        modules.module_output(model)
        return redirect('index')
    context['form'] = form
    return render(request, template_name, context)

@login_required
def glfunc(request):
    template_name = './journalentryapp/gl.html'
    model = JournalentryModel
    object_list = model.objects.all()
    print(object_list)
    data = pd.read_csv(filepath_or_buffer="journalentryapp/output/data.csv", encoding="UTF-8", sep=",")
    data['Dr.price'] = data['Dr.price'].astype(np.int64)
    data['Cr.price'] = data['Cr.price'].astype(np.int64)
    account_list = []
    for account in data['Dr.account']:
        if account not in account_list:
            account_list.append(account)
    for account in data['Cr.account']:
        if account not in account_list:
            account_list.append(account)
    context = {
        'object_list': object_list,
        'account_list': account_list,
    }
    return render(request, template_name, context)
