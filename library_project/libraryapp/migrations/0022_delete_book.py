# Generated by Django 4.2.14 on 2024-07-14 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("libraryapp", "0021_alter_library_librarian"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Book",
        ),
    ]
