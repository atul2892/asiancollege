# Generated by Django 5.0.1 on 2024-05-07 11:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_admission_career_opportunities_admission_dress_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionYears',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
            ],
        ),
    ]
