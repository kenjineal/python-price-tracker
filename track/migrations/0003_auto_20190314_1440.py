# Generated by Django 2.1.7 on 2019-03-14 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20190314_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='current_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='yourprice',
            new_name='desire_price',
        ),
    ]
