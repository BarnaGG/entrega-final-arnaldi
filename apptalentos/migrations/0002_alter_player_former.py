# Generated by Django 5.1.1 on 2024-09-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptalentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='former',
            field=models.CharField(max_length=100),
        ),
    ]
