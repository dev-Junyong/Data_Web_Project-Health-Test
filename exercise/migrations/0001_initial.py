# Generated by Django 3.2.8 on 2021-11-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sports', models.CharField(max_length=200)),
                ('addr', models.CharField(max_length=300)),
                ('x_coord', models.FloatField()),
                ('y_coord', models.FloatField()),
                ('tel', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]