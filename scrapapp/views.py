from django.shortcuts import render,redirect
from django.views.generic import View
from scrapapp.models  import Scraps
from scrapapp.forms import  ScrapForm,RegistraionForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib .auth import authenticate,login,logout
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper    

#def method_decorator(decorator name,name=none)
@method_decorator(signin_required,name="dispatch")
class ScrapListView(View):
    def get(self,request,*args,**kwargs):
        qs=Scraps.objects.all()
       
        if "location"in request.GET:
            location=request.GET.get("location")
            qs=qs.filter(location__iexact=location)
        if "price_gt" in request.GET:
            amount=request.GET.get("price_gt")
            qs=qs.filter(price__gt=amount)
        if "category" in request.GET:
            category=request.GET.get("category")   
            qs=qs.filter(category__iexact=category)
        return render(request,"scrap_list.html",{"data":qs})
        


# localhost:8000/scraps/{id}    
@method_decorator(signin_required,name="dispatch")
class ScrapDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Scraps.objects.get(id=id)
        return render(request,"scrap_detail.html",{"data":qs})    
@method_decorator(signin_required,name="dispatch")  
class ScrapDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk") 
        Scraps.objects.get(id=id).delete() 
        messages.success(request,"deleted successfully")  
        return redirect("scrap-all")
@method_decorator(signin_required,name="dispatch") 
class ScrapCreateView(View):
    def get(self,request,*args,**kwargs):
        form= ScrapForm()  
        return render(request,"scrap_add.html",{"form":form})  
     
    def post(self,request,*args,**kwargs):
        form=ScrapForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully created")
            return redirect("scrap-all")
        else:
            messages.error(request,"created successfully")
            return render(request,"scrap_add.html",{"form":form})  
@method_decorator(signin_required,name="dispatch")       
class ScrapUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")  
        obj=Scraps.objects.get(id=id)
        form=ScrapForm(instance=obj)
        return render(request,"scrap_edit.html",{"form":form})    
  
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Scraps.objects.get(id=id)
        form=ScrapForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"updated successfully")
            return redirect("scrap-all")
        else:
            return render(request,"scrap_edit.html",{"form":form}) 

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistraionForm()
        return render(request,"register.html",{"form":form})   
    def post(self,request,*args,**kwargs):
        form=RegistraionForm(request.POST)
        if form.is_valid():
            #form.save()
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"account created successfully")
            return render(request,"register.html",{"form":form})   
        else:
            messages.error(request,"failed to create the account")  
            return render(request,"register.html",{"form":form})    
      
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)#initializing using value in post
        if form.is_valid():
            uname=form.cleaned_data.get("username")#extracting username and password
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(username=uname,password=pwd)#checking whether credentials are correct
            if user_object:#if there is user object
                print("valid credentials")
                login(request,user_object)#start user session if user is valid
                print(request.user)#fetch user details
                return redirect("scrap-all")#redircting to listing page
            else:
                print("invalid credentials")    
            return render(request,"register.html",{"form":form})   
        else:
           
           return render(request,"register.html",{"form":form})   
        
@method_decorator (signin_required,name="dispatch")   
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    

        

        



