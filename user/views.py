from django.shortcuts import render
from user.models import User
from user.models import Post
from datetime import datetime
# Create your views here.
def user(request):

    if request.method == "POST":
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        email = request.POST.get("email")
        password= request.POST.get("password")
        user_name= request.POST.get("user_name")
       
        user =  User(first_name=first_name,last_name=last_name, email=email,password=password,user_name=user_name)
        user.save()

    return render(request,'user.html')



def post(request):

    if request.method == "POST":
        user =request.POST.get('user')
        text =request.POST.get('last_name')
        post=Post(user=user,text=text,created_at=datetime.today(),updated_at = datetime.today)
        post.save()


    return render (request,"post.html")