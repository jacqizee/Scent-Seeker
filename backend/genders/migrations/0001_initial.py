# Generated by Django 4.1 on 2022-08-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('F', 'Feminine'), ('M', 'Masculine'), ('U', 'Unisex')], max_length=10)),
            ],
        ),
    ]
