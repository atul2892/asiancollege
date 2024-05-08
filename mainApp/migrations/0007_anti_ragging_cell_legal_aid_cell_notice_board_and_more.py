# Generated by Django 5.0.1 on 2024-05-07 10:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_facilitie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anti_Ragging_Cell',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Legal_Aid_Cell',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice_Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ref_no', models.CharField(max_length=10)),
                ('details', models.TextField()),
                ('date', models.CharField(max_length=100)),
                ('downloads', models.FileField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
            ],
        ),
    ]