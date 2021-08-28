# Generated by Django 3.2.4 on 2021-08-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hospitallist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(max_length=50)),
                ('ghph', models.CharField(max_length=15)),
                ('specialty', models.CharField(max_length=10)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=10)),
                ('contactno', models.IntegerField()),
                ('mailid', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]