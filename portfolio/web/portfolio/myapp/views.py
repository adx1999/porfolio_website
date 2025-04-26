from django.shortcuts import render
from .models import User

# Create your views here.
def form(request):
    
    if request.method =="POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        message = request.POST.get("Message")
        print(name,email,message)
        contact = User(name=name,email=email,message =message)
        contact.save()
        
    return render(request,'index.html')


