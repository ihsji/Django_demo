# Generated by Django 5.1.1 on 2024-09-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("老师姓名", models.CharField(max_length=50)),
                ("手机号码", models.CharField(max_length=11, unique=True)),
                ("性别", models.CharField(max_length=1)),
                ("出生日期", models.DateField()),
            ],
        ),
    ]
