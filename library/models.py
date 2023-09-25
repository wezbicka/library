from django.db import models


class Reader(models.Model):
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)
    patronymic = models.CharField("Отчество", max_length=20)

    def __str__(self):
        return self.surname
    
    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=200)

    def __str__(self):
        return f'{self.id} {self.author} "{self.title}"'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


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
    return_date = models.DateTimeField("Дата возврата", null=True, blank=True)
    was_returned = models.BooleanField("Возвращена", default=False)

    def __str__(self):
        return '{reader} брал книгу {book} c {borrow_date} {returned}'.format(
            reader=self.reader,
            book=self.book,
            borrow_date=self.borrow_date,
            returned=(
                f'по {self.return_date}'
                if self.return_date else 'и не вернул'
            )
        )

    class Meta:
        verbose_name = 'Движение книги'
        verbose_name_plural = 'Движения книг'
