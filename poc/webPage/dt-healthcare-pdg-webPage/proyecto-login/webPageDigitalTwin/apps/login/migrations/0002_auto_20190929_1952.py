# Generated by Django 2.2.5 on 2019-09-30 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctor',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='passwordDoctor',
            new_name='password',
        ),
    ]
