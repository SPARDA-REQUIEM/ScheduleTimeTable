# Generated by Django 4.1.3 on 2022-11-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='facultyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputId', models.CharField(max_length=4)),
                ('inputName', models.CharField(max_length=100)),
                ('inputContactNumber', models.CharField(max_length=11)),
            ],
        ),
    ]
