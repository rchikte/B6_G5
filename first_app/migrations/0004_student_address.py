# Generated by Django 4.0.1 on 2022-01-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_student_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]