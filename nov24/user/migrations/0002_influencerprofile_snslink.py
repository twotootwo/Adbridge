# Generated by Django 4.2.16 on 2024-11-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencerprofile',
            name='snslink',
            field=models.URLField(blank=True, null=True),
        ),
    ]