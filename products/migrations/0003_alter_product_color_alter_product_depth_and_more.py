# Generated by Django 5.1 on 2024-08-15 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_productimages_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='depth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_type',
            field=models.CharField(choices=[('fix', 'Fix'), ('percentage', 'Percentage')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='made_in',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
