# Generated by Django 5.1.2 on 2024-10-28 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("car_number", models.CharField(max_length=15)),
                ("brand", models.CharField(max_length=20)),
                ("car_model", models.CharField(max_length=20)),
                ("colour", models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Owner",
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
                ("last_name", models.CharField(max_length=30)),
                ("first_name", models.CharField(max_length=30)),
                ("date_of_birth", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="License",
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
                ("license_number", models.CharField(max_length=10)),
                ("license_type", models.CharField(max_length=10)),
                ("receiving_date", models.DateField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project_first_app.owner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ownership",
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
                ("beginning", models.DateField()),
                ("ending", models.DateField(blank=True, null=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project_first_app.car",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project_first_app.owner",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="owner",
            name="cars",
            field=models.ManyToManyField(
                through="project_first_app.Ownership", to="project_first_app.car"
            ),
        ),
    ]