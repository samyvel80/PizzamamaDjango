# Generated by Django 3.2.16 on 2023-02-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20230213_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='user',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='nom',
            field=models.CharField(max_length=200),
        ),
    ]
