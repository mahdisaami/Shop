# Generated by Django 2.2 on 2020-09-13 17:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='created time')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('price', models.FloatField(verbose_name='price')),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('available', models.BooleanField(default=True, verbose_name='available')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.Category', verbose_name='category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='created time')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stars', to='product.Product', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stars', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Star',
                'verbose_name_plural': 'Stars',
                'db_table': 'star',
            },
        ),
        migrations.CreateModel(
            name='PrAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='created time')),
                ('value', models.CharField(max_length=32, verbose_name='value')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr_attributes', to='category.CatAttribute', verbose_name='name')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr_attribute', to='product.Product', verbose_name='pr attribute')),
            ],
            options={
                'verbose_name': 'PrAttribute',
                'verbose_name_plural': 'PrAttributes',
                'db_table': 'pr_attribute',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='created time')),
                ('media_type', models.PositiveSmallIntegerField(choices=[(0, 'image'), (1, 'video')], default=0, verbose_name='media type')),
                ('media_file', models.FileField(upload_to='content/media', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'mp4', 'wmv', 'flv', 'png'))], verbose_name='media file')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Medias',
                'db_table': 'media',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='created time')),
                ('text', models.TextField(verbose_name='text')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='product.Product', verbose_name='product')),
                ('reply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='product.Comment', verbose_name='reply to')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comment',
            },
        ),
    ]
