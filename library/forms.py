from django import forms

from .models import Reader


class Login(forms.Form):
    readers = Reader.objects.all()
    choices = [(reader.surname, reader.surname) for reader in readers]
    username = forms.ChoiceField(
        label='Фамилия',
        choices=choices,
        widget=forms.Select(attrs={
            'class': 'form-control', 
        })
    )
    password = forms.CharField(
        label='Пароль', max_length=75, required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )


class Registration(forms.Form):
    surname = forms.CharField(
        label='Фамилия', max_length=75, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите фамилию пользователя'
        })
    )
    name = forms.CharField(
        label='Имя', max_length=75, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя'
        })
    )
    patronymic = forms.CharField(
        label='Отчество', max_length=75, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите отчество'
        })
    )
    password = forms.CharField(
        label='Пароль', max_length=75, required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )


class ActionBook(forms.Form):
    code = forms.IntegerField(
        label="Код книги",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите код книги'
        })
    )
