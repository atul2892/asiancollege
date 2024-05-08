# Generated by Django 5.0.1 on 2024-05-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_studentregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_Prospectus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='notice_board',
            name='downloads',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
