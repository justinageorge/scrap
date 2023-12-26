from django import forms
from scrapapp.models import Scraps
from django.contrib.auth.models import User


class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scraps
        fields="__all__"
        widgets={"name":forms.TextInput(attrs={"class":"form-control"}),
                 "category":forms.TextInput(attrs={"class":"form-control"}),
                 "price":forms.NumberInput(attrs={"class":"form-control"}),
                 "location":forms.TextInput(attrs={"class":"form-control"})
                 }
        
class RegistraionForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username",'email',"password"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=(forms.TextInput(attrs={"class":"form-control"})))
    password=forms.CharField(widget=(forms.PasswordInput(attrs={"class":"form-control"})))        