from django.shortcuts import redirect, render
from django.views import View
from django import forms

from django.contrib.auth import authenticate, login

from .forms import Login


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = Login()
        return render(request, "login.html", context={
            'form': form
        })

    def post(self, request):
        form = Login(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("reader_account")

        return render(request, "login.html", context={
            'form': form,
            'ivalid': True,
        })


