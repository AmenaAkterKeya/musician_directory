# Generated by Django 5.0.6 on 2024-05-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='phone',
            field=models.CharField(max_length=120),
        ),
    ]
