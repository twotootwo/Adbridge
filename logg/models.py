from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, position, password=None):
        if not username:
            raise ValueError('Must have a username')
        if not position:
            raise ValueError('Must have an position')
        user = self.model(
            username=username,
            position = position,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, position, password):
        if not username:
            raise ValueError('Must have a username')
        if not position:
            raise ValueError('Must have an email address')
        user = self.create_user(
            username,
            position,
            password
        )
        user.is_admin = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=128, unique=True)
    position = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = True

    def has_module_perms(self, *args, **kwargs):
        return True

    def has_perm(self, *args, **kwargs):
        return True

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password','position']

    def __str__(self):
        return self.username+" "+self.position

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # primary_key를 user의 pk로 설정
    nickname = models.CharField(max_length=128, null=False, blank=False, default='Default_Nickname')
    position = models.CharField(max_length=128)  # 광고주인지 인플루언서인지
    subjects = models.CharField(max_length=128)  # 관심사
    image = models.ImageField(upload_to='profile/', default='default.jpg')  # 이미지 등록
    REQUIRED_FIELDS = ['nickname','position','subjects']

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(
#             user=instance,
#             nickname=f'User_{instance.id}',  # 기본 닉네임
#             position='Undefined',          # 기본 포지션
#             subjects='None',               # 기본 관심사
#         )







