from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from Adminapp.models import *
from django.db.models.aggregates import Sum


# Create your views here.
def index(request):
    data = Branchdb.objects.all()
    return render(request,'index.html',{'data':data})   

def about(request):
    return render(request,'about.html')  

def contact(request):
    return render(request,'contact.html')  

   
def login(request):
    return render(request,'login.html') 

def branches(request):
    data = Branchdb.objects.all()
    return render(request,'branches.html',{'data':data})    

def services(request):
    data = Serverdb.objects.all()
    return render(request,'services.html',{'data':data})    
          

def getValue(request):
    if request.method=="POST":
        message = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        data = Contactdb(message=message,name=name,email=email,subject=subject)
        data.save()
        return redirect('contact')

def registration(request):
    return render(request,"registration.html")

def getRegister(request):
    if request.method=="POST":
       firstname = request.POST.get('firstname')
       lastname = request.POST.get('lastname')
       phone = request.POST.get('phone')
       email = request.POST.get('email')
       username = request.POST.get('username')
       password = request.POST.get('password')
       data = Registrationdb(firstname=firstname,lastname=lastname,phone=phone,email=email,username=username,password=password)
       data.save()
       return redirect('registration')    

def getLogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Registrationdb.objects.filter(username=username,password=password).exists():
            data = Registrationdb.objects.filter(username=username,password=password).values('firstname','lastname','phone','email','id').first()
            request.session['username_u'] = username
            request.session['password_u'] = password
            request.session['u_firstname'] = data['firstname']
            request.session['u_lastname'] = data['lastname']
            request.session['u_phone'] = data['phone']
            request.session['u_email'] = data['email']
            request.session['id'] = data['id']

            return redirect('index')
        else:
            return render(request,'login.html',{'msg':'Invalid user credentials'})    
        
    else:
        return redirect('index')

def productdetails(request):
    return render(request,'productdetails.html') 

def viewdetails(request, branchname):
    data = Serverdb.objects.filter(branch=branchname)
    return render(request,'viewdetails.html',{'data':data})   

def cart(request):
    u = request.session.get('id')
    data = Cartdb.objects.filter(userid=u,status=0)
    y = Cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    x = y['total__sum']
    print(x)
    return render(request,'cart.html',{'data':data,'x':x}) 

          
def getCart(request):
    if request.method=="POST":
        print("hello")
        serviceid = request.POST.get('serviceid')
        userid = request.session.get('id')
        price = request.POST.get('price')
        status = 0
        data = Cartdb(serviceid=Serverdb.objects.get(id=serviceid),userid=Registrationdb.objects.get(id=userid),total=price,status=status)
        data.save()
        return redirect('cart')    
       
def logout(request):
    del request.session['username_u']
    del request.session['password_u']
    del request.session['u_firstname']
    del request.session['u_lastname']
    del request.session['u_phone']
    del request.session['u_email']
    del request.session['id']
    return redirect('index')

def checkout(request):
    u = request.session.get('id')
    data = Cartdb.objects.filter(userid=u,status=0)
    y = Cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    x = y['total__sum']
    print(x)
    return render(request,'checkout.html',{'data':data,'x':x})
   
        
        
    

def getBooking(request):
    if request.method=="POST":
        date = request.POST.get('date')
        time = request.POST.get('time')
        userid = request.session.get('id')
        order = Cartdb.objects.filter(userid=userid,status=0)
        for i in order:
            data=Bookingdb(cartid=Cartdb.objects.get(id=i.id),userid=Registrationdb.objects.get(id=userid),date=date,time=time)
            data.save()
            Cartdb.objects.filter(id=i.id).update(status=1)
        return redirect('index') 
        
def cartdelete(request,did):
    Cartdb.objects.filter(id=did).delete()
    return redirect('cart')       
