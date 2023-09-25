from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Reader, Book, Borrowing


admin.site.register(Reader)
admin.site.register(Borrowing)
admin.site.register(Book)

