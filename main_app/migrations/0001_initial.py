# Generated by Django 4.2.1 on 2023-05-31 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
    ]