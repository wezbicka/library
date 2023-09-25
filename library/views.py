from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate, login

from .forms import Login, Registration
from .models import Reader


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


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = Registration()
        return render(request, "signup.html", context={
            'form': form
        })

    def post(self, request):
        form = Registration(request.POST)

        if form.is_valid():
            surname = form.cleaned_data['surname']
            name = form.cleaned_data['name']
            patronymic = form.cleaned_data['patronymic']
            password = make_password(form.cleaned_data['password'])
            created, reader = Reader.objects.get_or_create(
                surname=surname,
                name=name,
                patronymic=patronymic,
            )
            created_user, user = User.objects.get_or_create(
                username=surname,
                first_name=name,
                password=password,
            )

            user = authenticate(request, username=surname, password=password)
            if user:
                login(request, user)
                return redirect("reader_account")

        return render(request, "login.html", context={
            'form': form,
            'ivalid': True,
        })
