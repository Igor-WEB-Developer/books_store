# Generated by Django 2.2.19 on 2022-12-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20221222_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, help_text='загрузите картинку книги', null=True, upload_to='photos/', verbose_name='фото книги'),
        ),
    ]
