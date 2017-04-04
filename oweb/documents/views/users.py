from django.shortcuts import render
from django.http import HttpResponse

from documents.models import UserProfile
from django import forms

class Form_inscription(forms.Form):
     name = forms.CharField(label="Name", max_length=30)
     login = forms.CharField(label="Login", max_length=30)
     password = forms.CharField(label="Password",widget=forms.PasswordInput)

def page(request):
    if request.POST:
        form = Form_inscription(request.POST)
        if form.is_valid():
            name        = form.cleaned_data['name']
            login       = form.cleaned_data['login']
            password    = form.cleaned_data['name']

            new_user = UserProfile(name=name, login=login, password=password)
            new_user.save()
            return HttpResponse('User added')
        else:
            return render(request, 'create_user.html', {'form':form})
    else:
        form = Form_inscription()
        return render(request, 'create_user.html', {'form':form})