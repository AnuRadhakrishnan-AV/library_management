# Generated by Django 4.2.14 on 2024-07-14 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("libraryapp", "0013_alter_library_image_alter_library_librarian"),
    ]

    operations = [
        migrations.AlterField(
            model_name="library",
            name="librarian",
            field=models.ForeignKey(
                limit_choices_to={"role": "librarian"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="libraryapp.user",
            ),
        ),
    ]
