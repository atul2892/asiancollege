# Generated by Django 5.0.1 on 2024-05-07 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_academics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Academics',
            new_name='Academic',
        ),
    ]
