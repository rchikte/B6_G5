# Generated by Django 4.0.1 on 2022-01-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first_app', '0006_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marks', models.FloatField()),
                ('subject', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]