# Generated by Django 4.0.3 on 2022-06-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0005_alter_category_cat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(null=True, upload_to='Category_images/', verbose_name='Category Photo'),
        ),
    ]
