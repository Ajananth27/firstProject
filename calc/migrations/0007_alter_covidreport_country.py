# Generated by Django 3.2.4 on 2021-08-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_auto_20210817_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidreport',
            name='country',
            field=models.CharField(max_length=30),
        ),
    ]
