from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# profile model로 모델 확장하기
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # primary_key를 user의 pk로 설정
    nickname = models.CharField(max_length=128)  # 닉네임
    position = models.CharField(max_length=128)  # 광고주인지 인플루언서인지
    subjects = models.CharField(max_length=128)  # 관심사
    image = models.ImageField(upload_to='profile/', default='default.jpg')  # 이미지 등록


# @receiver(post_save, sender=User)  # 알아서 유저 생성 이벤트를 감지해 프로필을 자동으로 생성해줌
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            nickname=f'User_{instance.id}',  # 기본 닉네임
            position='Undefined',          # 기본 포지션
            subjects='None',               # 기본 관심사
        )

