# Generated by Django 3.2.7 on 2021-09-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bkg', '0003_auto_20210912_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]