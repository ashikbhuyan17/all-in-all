# Generated by Django 2.2.13 on 2020-11-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0019_auto_20201129_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='tuition/images'),
        ),
    ]
