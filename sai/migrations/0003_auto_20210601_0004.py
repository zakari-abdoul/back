# Generated by Django 3.2.3 on 2021-06-01 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sai', '0002_auto_20210520_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sai_in',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sai_out',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
