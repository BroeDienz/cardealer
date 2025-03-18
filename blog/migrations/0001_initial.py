# Generated by Django 5.1.6 on 2025-02-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('register', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.IntegerField()),
                ('vin', models.CharField(max_length=100)),
            ],
        ),
    ]
