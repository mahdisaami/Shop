# Generated by Django 2.2 on 2020-10-08 12:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20201008_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('3667a643-6b74-4c17-b3d8-f1d05a51e830'), editable=False, unique=True, verbose_name='uuid'),
        ),
    ]
