# Generated by Django 5.1.3 on 2024-11-25 09:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_influencerprofile_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='influencerprofile',
            name='post_id',
        ),
        migrations.AddField(
            model_name='advertiserprofile',
            name='post_account',
            field=models.ForeignKey(db_column='email_account', default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencerprofile',
            name='post_account',
            field=models.ForeignKey(db_column='email_account', default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
