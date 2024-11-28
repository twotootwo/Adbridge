# Generated by Django 5.1.3 on 2024-11-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=128, unique=True)),
                ("position", models.CharField(max_length=128)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Advertisement",
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
                (
                    "thumbnail",
                    models.ImageField(
                        default="product.svg", upload_to="advertisement/"
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("product_name", models.CharField(max_length=128)),
                ("description", models.TextField(default="description of the product")),
                ("min_budget", models.PositiveIntegerField(default=0)),
                ("max_budget", models.PositiveIntegerField(default=0)),
                (
                    "product_image",
                    models.ImageField(
                        default="product.svg", upload_to="advertisement/"
                    ),
                ),
            ],
        ),
    ]