# Generated by Django 5.1.3 on 2024-11-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='advertiserprofile',
            name='thumbnail',
            field=models.ImageField(default='product.svg', upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='field',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('food', 'Food'), ('health', 'Health'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='position',
            field=models.CharField(choices=[('influencer', 'Influencer'), ('advertiser', 'Advertiser')], max_length=50),
        ),
        migrations.AlterField(
            model_name='influencerprofile',
            name='thumbnail',
            field=models.ImageField(default='product.svg', upload_to='profile/'),
        ),
    ]
