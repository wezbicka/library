from django.contrib import admin

from .models import Reader, Book, Borrowing


# @admin.register(Reader)
# class ReaderAdmin(admin.ModelAdmin):
#     field = ("")


# @admin.register(Borrowing)
# class BorrowingAdmin(admin.ModelAdmin):


admin.site.register(Borrowing)
admin.site.register(Book)
admin.site.register(Reader)
