# Generated by Django 4.1.1 on 2022-09-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=4)),
                ('watering_week', models.IntegerField()),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
