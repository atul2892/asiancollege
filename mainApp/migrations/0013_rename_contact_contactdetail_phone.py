# Generated by Django 5.0.1 on 2024-05-08 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_contactdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdetail',
            old_name='contact',
            new_name='phone',
        ),
    ]
