# Generated by Django 2.2 on 2020-09-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200916_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='user/avatar/', verbose_name='avatar'),
        ),
    ]