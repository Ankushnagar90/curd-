from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregister
from django import forms
from .models import Person
# Create your views here.
def home(request):
    if request.method =='POST':
        fm = studentregister(request.POST)
        if fm.is_valid():
            fnm = fm.cleaned_data['first_name']
            lnm = fm.cleaned_data['last_name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg=Person(first_name=fnm,last_name=lnm,email=em,password=pwd)
            reg.save()
            fm=studentregister()

    else:
        fm=studentregister()

    stud = Person.objects.all()
    return render(request, 'crud/addstudent.html',{'form':fm,'stu':stud})  



#update function 

def update_data(request,id):
    if request.method == 'POST':
        pi = Person.objects.get(pk=id)
        fm=studentregister(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Person.objects.get(pk=id)
        fm = studentregister(instance=pi)
    return render(request,'crud/updatestu.html',{'form':fm})


# Delete function:
def delete_data(request,id):
    if request.method == 'POST':
        pi=Person.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')