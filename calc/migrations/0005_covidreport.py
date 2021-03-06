# Generated by Django 3.2.4 on 2021-08-17 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_alter_hospitallist_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='covidreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
                ('totalcases', models.IntegerField()),
                ('newcases', models.CharField(max_length=20)),
                ('totaldeaths', models.IntegerField()),
                ('newdeaths', models.CharField(max_length=10)),
                ('totalrecovered', models.IntegerField()),
                ('newrecovered', models.CharField(max_length=10)),
                ('activecases', models.IntegerField()),
            ],
        ),
    ]
