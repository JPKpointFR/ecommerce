# Generated by Django 4.1.5 on 2023-01-02 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=200)),
                ("date_added", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-date_added"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200)),
                ("price", models.FloatField()),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to=None)),
                ("date_added", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categorie",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "ordering": ["-date_added"],
            },
        ),
    ]
