# Generated by Django 2.2.5 on 2019-09-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('passwordDoctor', models.CharField(max_length=40)),
            ],
        ),
    ]
