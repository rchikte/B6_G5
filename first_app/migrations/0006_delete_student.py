# Generated by Django 4.0.1 on 2022-01-24 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_student_is_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]