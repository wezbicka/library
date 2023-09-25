# Generated by Django 4.2.5 on 2023-09-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='borrowing',
            options={'verbose_name': 'Движение книги', 'verbose_name_plural': 'Движения книг'},
        ),
        migrations.AlterModelOptions(
            name='reader',
            options={'verbose_name': 'Читатель', 'verbose_name_plural': 'Читатели'},
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='return_date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Дата возврата'),
        ),
    ]
