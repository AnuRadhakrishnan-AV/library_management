# Generated by Django 4.2.14 on 2024-07-13 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("libraryapp", "0009_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="library",
            name="librarian",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"role": "librarian"},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="libraries",
                to="libraryapp.user",
            ),
        ),
    ]
