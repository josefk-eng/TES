# Generated by Django 4.2.1 on 2023-06-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kisi", "0004_kreview_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kreview",
            name="text",
            field=models.CharField(default="", max_length=1000),
        ),
    ]