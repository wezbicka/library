from django.db import models


class Reader(models.Model):
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)
    patronymic = models.CharField("Отчество", max_length=20)

    def __str__(self):
        return self.surname


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=200)

    def __str__(self):
        return f"{self.title} {self.author}"


class Borrowing(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="borrowing_records",
    )
    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE,
        related_name="borrowing_records",
    )
    borrow_date = models.DateTimeField("Дата выдачи")
    return_date = models.DateTimeField("Дата возврата")
    was_returned = models.BooleanField("Возвращена", default=False)
