from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.

def map(request):
    return render(request, 'map.html')

def register(request):
    
    if request.method =='POST':
        id = request.POST['id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(id=id,fname=fname,lname=lname,password=password,email=email)
        user.save()
        print("user c")
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def process(request):
    return render(request, 'process.html')