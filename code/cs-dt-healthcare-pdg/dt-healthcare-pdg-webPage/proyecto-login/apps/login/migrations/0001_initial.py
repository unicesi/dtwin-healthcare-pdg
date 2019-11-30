# Generated by Django 2.2.6 on 2019-11-19 13:57

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=40)),
                ('identificationCard', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('size_patient', models.DecimalField(decimal_places=2, max_digits=4)),
                ('age', models.IntegerField()),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
    ]
