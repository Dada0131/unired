# Generated by Django 4.2.16 on 2024-11-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialpost',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
