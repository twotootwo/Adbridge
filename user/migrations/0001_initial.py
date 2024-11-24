# Generated by Django 5.1.3 on 2024-11-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('position', models.CharField(choices=[('influencer', 'Influencer'), ('advertiser', 'Advertiser')], max_length=128)),
                ('username', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nickname', models.CharField(max_length=128, unique=True)),
                ('field', models.CharField(choices=[('fashion', 'Fashion'), ('food', 'Food'), ('health', 'Health'), ('other', 'Other')], max_length=128)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdvertiserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InfluencerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(default='product.svg', upload_to='advertisement/')),
                ('contents', models.CharField(max_length=128)),
                ('method', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=128)),
                ('detail_1', models.ImageField(default='product.svg', upload_to='profile/')),
                ('description', models.TextField(default='description of the person')),
                ('detail_2', models.ImageField(default='product.svg', upload_to='profile/')),
            ],
        ),
    ]
