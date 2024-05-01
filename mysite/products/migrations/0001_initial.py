# Generated by Django 5.0.4 on 2024-04-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=11)),
                ('age', models.IntegerField(default=0)),
                ('national_number', models.CharField(max_length=20)),
            ],
        ),
    ]
