# Generated by Django 4.1.5 on 2023-01-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
    ]
