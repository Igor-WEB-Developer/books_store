# Generated by Django 2.2.19 on 2022-12-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default=0, help_text='Добавьте фото', upload_to='', verbose_name='Фото'),
        ),
    ]