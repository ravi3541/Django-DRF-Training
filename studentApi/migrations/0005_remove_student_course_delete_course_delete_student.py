# Generated by Django 4.0.4 on 2022-06-03 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApi', '0004_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
