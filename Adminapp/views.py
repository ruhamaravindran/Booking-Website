from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from UserApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def adminindex(request):
    user_count = Registrationdb.objects.all().count()
    booking_count = Bookingdb.objects.all().count()
    branches_count = Branchdb.objects.all().count()
    services_count = Serverdb.objects.all().count()
    messages_count = Contactdb.objects.all().count()
    data = Contactdb.objects.all()
    return render(request,'adminindex.html',{'user_count':user_count,'booking_count':booking_count,'branches_count':branches_count,'services_count':services_count,'messages_count':messages_count,'data':data})
    
def addbranches(request):
    return render(request,'addbranches.html')

def getData(request):
    if request.method=="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES['image']
        data = Branchdb(name=name,description=description,image=image)
        data.save()
        return redirect('addbranches')

def viewbranches(request):
    data = Branchdb.objects.all()
    return render(request,'viewbranches.html',{'data':data} )   

def delete(request,did):
    Branchdb.objects.filter(id=did).delete()
    return redirect('viewbranches')

def branch_edit(request,did):
    data = Branchdb.objects.filter(id=did)
    return render(request,'branch_edit.html',{'data':data})

def branchupdate(request,did):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file = Branchdb.objects.get(id=did).image
        Branchdb.objects.filter(id=did).update(name=name,description=description,image=file)
        return redirect('viewbranches')

def addservices(request):
    data=Serverdb.objects.all()
    return render(request,'addservices.html',{'data':data} )

def getDetails(request):
    if request.method=="POST":
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        price = request.POST.get('price')
        image = request.FILES['image']
        data = Serverdb(name=name,branch=branch,price=price,image=image)
        data.save()
        return redirect('addservices')

def viewservices(request):
    data = Serverdb.objects.all()
    return render(request,'viewservices.html',{'data':data} )   

def servicedelete(request,did):
    Serverdb.objects.filter(id=did).delete()
    return redirect('viewservices')

def serviceedit(request,did):
    data = Serverdb.objects.filter(id=did)
    branch = Branchdb.objects.all()
    return render(request,'serviceedit.html',{'data':data,'branch':branch}) 

def update(request,did):
    if request.method == "POST":
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        price = request.POST.get('price')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file = Serverdb.objects.get(id=did).image
        Serverdb.objects.filter(id=did).update(name=name,branch=branch,price=price,image=file)
        return redirect('viewservices')

def viewuser(request):
    data = Registrationdb.objects.all()
    return render(request,'viewuser.html',{'data':data} ) 

def viewappoinments(request):
    data = Bookingdb.objects.all()
    return render(request,'viewappoinments.html',{'data':data} ) 

    
def viewmessages(request):
    data = Contactdb.objects.all()
    return render(request,'viewmessages.html',{'data':data} ) 

def adminlogin(request):
    return render(request,'adminlogin.html')

def getAdmin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            return redirect('adminindex')
        else:
            return render(request,'adminlogin.html',{'msg':'Invalid user credentials'})
    else:
         return render(request,'adminlogin.html',{'msg':'Invalid user credentials'})
 
def adminlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    return redirect('adminlogin') 
 


 
    
        



