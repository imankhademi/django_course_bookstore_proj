# Generated by Django 4.1.5 on 2023-01-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_remove_comment_recommend'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
    ]