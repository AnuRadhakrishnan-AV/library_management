# Generated by Django 4.2.14 on 2024-07-15 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("libraryapp", "0024_alter_book_isbn"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="publication_date",
        ),
    ]
