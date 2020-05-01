# Generated by Django 3.0.5 on 2020-04-27 02:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20200426_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='quantity',
            field=models.IntegerField(blank=1),
        ),
    ]