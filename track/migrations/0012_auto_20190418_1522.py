# Generated by Django 2.1.7 on 2019-04-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0011_auto_20190323_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_url',
            field=models.URLField(max_length=1000),
        ),
    ]
