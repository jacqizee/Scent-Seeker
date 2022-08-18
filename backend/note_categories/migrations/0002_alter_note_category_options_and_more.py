# Generated by Django 4.1 on 2022-08-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note_category',
            options={'verbose_name': 'Note Category', 'verbose_name_plural': 'Note Categories'},
        ),
        migrations.AlterField(
            model_name='note_category',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]