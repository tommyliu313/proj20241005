# Generated by Django 4.2 on 2024-10-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='warehouse',
            field=models.IntegerField(),
        ),
    ]
