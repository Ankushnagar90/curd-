from django.shortcuts import render
from .forms import studentregister
from django import forms
# Create your views here.
def home(request):
    if request.method =='POST':
        form=studentregister(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=studentregister()
    return render(request, 'crud/updatestu.html',{'form':form})