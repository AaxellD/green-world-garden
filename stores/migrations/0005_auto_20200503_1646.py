# Generated by Django 3.0.5 on 2020-05-03 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_store_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='zipcode',
            field=models.IntegerField(default=0),
        ),
    ]