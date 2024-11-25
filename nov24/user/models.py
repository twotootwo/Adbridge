from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db.models import CASCADE


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,password, **extra_fields):
        if not email:
            raise ValueError("The email is not given.")
        email= self.normalize_email(email)
        user= self.model(email=email, **extra_fields)
        user.is_active=True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    POSITION_CHOICES = (
        ('influencer', 'Influencer'), ('advertiser', 'Advertiser')
    )
    FIELD_CHOICES = (
        ('fashion', 'Fashion'), ('food', 'Food'), ('health', 'Health'), ('other', 'Other'),
    )
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)  # 광고주 또는 인플루언서 선택
    nickname = models.CharField(max_length=50, unique=True) #(회사명이나 인플러언서 활동명)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    field = models.CharField(max_length=50, choices=FIELD_CHOICES)  # 관심사
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname'] # used in create superuser

    objects = UserManager()

    def __str__(self):
        return self.nickname

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True


class InfluencerProfile(models.Model):
    #user = models.OneToOneField(CustomUser, on_delete=CASCADE, primary_key=True)
    post_account = models.ForeignKey(CustomUser, on_delete=CASCADE, blank=True)
    thumbnail = models.ImageField(upload_to='profile/', default='product.svg')
    contents = models.CharField(max_length=128, blank=True)
    method = models.CharField(max_length=128, blank=True)
    min_price = models.PositiveIntegerField(default=0)
    max_price = models.PositiveIntegerField(default=0)
    detail_1 = models.ImageField(upload_to='profile/', default='product.svg')
    description = models.TextField(default='description of the person')
    detail_2 = models.ImageField(upload_to='profile/', default='product.svg')

    def __str__(self):
        return self.contents


class AdvertiserProfile(models.Model):
    post_account = models.ForeignKey(CustomUser, on_delete=CASCADE, blank=True)
    thumbnail = models.ImageField(upload_to='profile/', default='product.svg')
    address = models.CharField(max_length=128, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.address
