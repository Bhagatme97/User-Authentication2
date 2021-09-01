from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.'
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'home.html')

def loginUser(request):

    if request.method=="POST":
        username=request.POST.get('name')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render( request,'login.html')
    return render( request,'login.html')

def logoutUser(request):
    return redirect("/login")

    # create user

def signupUser(request):
    
        if request.method=="POST":
            username=request.POST.get('name')
            password=request.POST.get('password')
        
            user = User.objects.create_user(username, 'noemail@noemail.com', password)

            user.save()
            # No backend authenticated the credentials
            return render( request,'login.html')
        return render(request,'signup.html')
    

def logoutUser(request):
    return redirect("/login")

    

    
        
