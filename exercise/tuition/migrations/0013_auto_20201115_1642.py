# Generated by Django 2.2.13 on 2020-11-15 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0012_auto_20201115_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='document',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='uploaded_at',
        ),
    ]
