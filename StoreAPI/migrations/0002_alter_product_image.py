# Generated by Django 4.2.1 on 2023-05-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("StoreAPI", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(default="productPH.png", upload_to="img/products"),
        ),
    ]
