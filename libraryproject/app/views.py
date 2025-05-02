from django.shortcuts import render, HttpResponse, redirect
from . models import Book
from django.contrib.auth.models import User
# Create your views here.



# def index(req):
# allbooks = Book.objects.all()
# print(allbooks)
# return HttpResponse(f'Allbooks')

from datetime import datetime


def index(req):
    allbooks = Book.objects.all()    #ORM
    print(allbooks)
    # context={"myname":"ITV"}
    # return render(req,'index.html',context)

    myname = "Neel"
    # return render(req,'index.html',{"myname" : myname})
    
    print(datetime.now())
    curdate = (datetime.now())
    hour = datetime.now().hour
    print(hour)
    context = {"myname" : myname, "curdate": curdate, "hour": hour, "allbooks": allbooks}    
    return render(req,'index.html', context)


def signup(req):
    print(req.method)   #GET
    if req.method=="GET":
        return render(req, "signup.html")
    else:
        print(req.method)   #POST
        uname = req.POST["uname"]
        uemail = req.POST["uemail"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        print(uname, upass, ucpass, uemail)
        if upass!=ucpass:
            errmsg=" Password and  Confirm Password must be same"
            context={'errmsg': errmsg}
            return render(req,'signup.html',context)
        elif uname == upass:
            errmsg = "Password should not be same as email id"
            context = {"errmsg": errmsg}
            return render(req, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, email=uemail, password=upass)
                userdata.set_password(upass)
                userdata.save()
                print(User.objects.all())
                return redirect("signin")
            except:
                errmsg = "User already exists!!! Try with different username"
                context = {"errmsg": errmsg}
                return render(req, "signup.html", context)

from django.contrib.auth import authenticate, login, logout

def signin(req):
    if req.method=="GET":
        print(req.method)
        return render(req, "signin.html")
    else:
        uname = req.POST.get("uname")
        uemail = req.POST.get('uemail')
        upass = req.POST["upass"]
        print(uname, uemail, upass)
        # userdata=User.objects.filter(email=uemail, password=upass)
        userdata=authenticate(username=uname, email=uemail, password=upass)
        print(userdata) # if matched with user then it show its id
        if userdata is not None:
            login(req, userdata)
            # return render((req, "dashboard.html"))
            return redirect("dashboard")
        else:
            context = {}
            context["errmsg"] = "Invalid email or password"
            return render(req, "signin.html", context)
        

def dashboard(req):
    print(req.user)
    username = req.user
    return render(req, "dashboard.html", {"username": username})

def userlogout(req):
    logout(req)
    return redirect('/')
