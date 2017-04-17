from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login

class Form_connection(forms.Form):
    username = forms.CharField(label="login")
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Form_connection, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong login or password")
        return self.cleaned_data

def page(request):
    if request.POST:
        form = Form_connection(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request, "authentication.html", {"user": user})
            else:
                return render(request, "authentication.html", {"form":form})
        else:
            form = Form_connection()
            return render(request, "authentication.html", {"form":form})
    else:
        form = Form_connection()
        return render(request, "authentication.html", {"form": form})
