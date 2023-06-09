# Generated by Django 4.2.1 on 2023-06-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="KProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "KProduct",
                "verbose_name_plural": "KProduct",
            },
        ),
        migrations.CreateModel(
            name="KReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.FloatField()),
            ],
            options={
                "verbose_name": "KReview",
                "verbose_name_plural": "KReview",
            },
        ),
    ]
