# Generated by Django 4.1.4 on 2022-12-24 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_remove_books_category_books_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="books",
            name="slug",
        ),
    ]
