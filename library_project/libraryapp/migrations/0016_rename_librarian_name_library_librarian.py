# Generated by Django 4.2.14 on 2024-07-14 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("libraryapp", "0015_remove_library_librarian_library_librarian_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="library",
            old_name="librarian_name",
            new_name="librarian",
        ),
    ]
