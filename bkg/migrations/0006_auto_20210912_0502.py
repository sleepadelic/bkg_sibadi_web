# Generated by Django 3.2.7 on 2021-09-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bkg', '0005_auto_20210912_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='geo_lat',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='geo_lon',
        ),
        migrations.AddField(
            model_name='issue',
            name='geo',
            field=models.CharField(max_length=300, null=True),
        ),
    ]