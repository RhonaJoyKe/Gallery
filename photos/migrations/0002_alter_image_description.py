# Generated by Django 3.2.9 on 2021-11-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]