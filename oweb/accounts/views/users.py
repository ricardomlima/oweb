from django.shortcuts import render
from accounts.models import UserProfile
from django import forms
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class UserForm(forms.Form):
    name = forms.CharField(label="Name", max_length=30)
    login = forms.CharField(label="Login", max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password_bis = forms.CharField(label="Password",widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data


class UserRegistrationView(View):
    form_class = UserForm
    template_name = "create_user.html"
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name        = form.cleaned_data['name']
            email       = form.cleaned_data['email']
            login       = form.cleaned_data['login']
            password    = form.cleaned_data['password']
            new_user = User.objects.create_user(username=login, email=email, password=password)
            new_user.is_active = True
            new_user.last_name = name
            new_user.save()
            new_userprofile = UserProfile(user_auth=new_user)
            new_userprofile.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, self.template_name, {'form':form})