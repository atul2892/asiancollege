# Generated by Django 5.0.1 on 2024-05-07 08:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facilitie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
            ],
        ),
    ]