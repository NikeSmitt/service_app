# Generated by Django 3.2.16 on 2023-10-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_services', '0002_auto_20231009_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='comment',
            field=models.CharField(default='', max_length=200),
        ),
    ]
