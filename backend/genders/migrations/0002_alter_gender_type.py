# Generated by Django 4.1 on 2022-08-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='type',
            field=models.CharField(max_length=15),
        ),
    ]
