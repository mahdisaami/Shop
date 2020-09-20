# Generated by Django 2.2 on 2020-09-20 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.ForeignKey(blank=True, max_length=32, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category', verbose_name='categories'),
        ),
    ]
