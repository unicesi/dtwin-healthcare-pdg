# Generated by Django 2.2.5 on 2019-09-30 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190929_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('size_patient', models.DecimalField(decimal_places=2, max_digits=4)),
                ('age', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='identificationCard',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]