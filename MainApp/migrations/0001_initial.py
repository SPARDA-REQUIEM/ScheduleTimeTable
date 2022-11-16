# Generated by Django 4.1.3 on 2022-11-16 01:10

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
                ('inputId', models.CharField(max_length=10)),
                ('inputName', models.CharField(max_length=100)),
                ('inputDepartment', models.CharField(max_length=100)),
                ('inputEmploymentStatus', models.CharField(max_length=100)),
                ('inputExpertiseSubject', models.CharField(max_length=100)),
                ('inputDayAvailability', models.CharField(max_length=100)),
                ('inputTimePreference', models.CharField(max_length=100)),
                ('inputUnitsLoad', models.CharField(max_length=100)),
            ],
        ),
    ]
