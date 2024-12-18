# Generated by Django 5.1.3 on 2024-11-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advertiserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
