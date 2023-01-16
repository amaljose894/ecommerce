# Generated by Django 4.1.3 on 2022-11-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_delete_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]