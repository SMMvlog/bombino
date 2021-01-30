# Generated by Django 3.1.5 on 2021-01-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awbNo', models.CharField(max_length=30)),
                ('actionDate', models.CharField(max_length=30)),
                ('actionTime', models.CharField(max_length=30)),
                ('exception', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('shipDate', models.DateField()),
            ],
        ),
    ]
