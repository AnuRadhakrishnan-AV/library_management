# Generated by Django 4.2.14 on 2024-07-17 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("libraryapp", "0033_user_is_approved_alter_library_library_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="library",
            name="librarian",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="libraryapp.user",
            ),
        ),
    ]
