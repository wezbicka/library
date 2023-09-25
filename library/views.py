from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import datetime

from django.contrib.auth import authenticate, login

from .forms import Login, Registration, ActionBook
from .models import Reader, Book, Borrowing


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


class BookView(View):
    def get(self, request):
        surname = request.user
        name = request.user.first_name
        reader = Reader.objects.get(surname=surname, name=name)
        borrowing_records = Borrowing.objects.filter(
            reader__surname=surname,
            reader__name=name
        )
        context = {
            "reader": reader,
            "borrowing_records": borrowing_records,
            # "books": [record.book for record in borrowing_records]
        }
        return render(request, 'books.html', context)


class ReturnBookView(View):
    def get(self, request, *args, **kwargs):
        form = ActionBook()
        return render(request, "return_book.html", context={
            'form': form
        })
    
    def post(self, request):
        form = ActionBook(request.POST)

        if form.is_valid():
            code = form.cleaned_data['code']
            book = Book.objects.get(id=code)
            borrowing_record = Borrowing.objects.filter(
                book=book
                ).update(
                    return_date=datetime.datetime.now(),
                    book__was_returned=True
                )
            return redirect("reader_account")
 
        return render(request, "return_book.html", context={
            'form': form,
            'ivalid': True,
        })


def free_book(request):
    books = Book.objects.filter(was_returned=True)
    return render(request, "free_books.html", context={
        "books": books
    })
