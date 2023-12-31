# Generated by Django 4.2.6 on 2023-10-23 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Voucher",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("numbers", models.IntegerField(default=0)),
                ("buy_amount", models.IntegerField(default=10)),
                ("get_amount", models.IntegerField(default=10)),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.store"
                    ),
                ),
            ],
        ),
    ]
