# Generated by Django 4.2.14 on 2024-07-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libraryapp", "0028_book_is_booked"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="returned_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
