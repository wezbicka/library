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
        label='Пароль', max_length=75, required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )
