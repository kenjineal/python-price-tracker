# Generated by Django 2.1.7 on 2019-03-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0007_auto_20190315_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_src',
            field=models.ImageField(upload_to=''),
        ),
    ]
