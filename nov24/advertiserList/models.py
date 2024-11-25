from django.db import models

class advertiserList(models.Model): # 광고주가 보는 리스트를 정의
    # 나의 광고 title, 인플루언서 nickname
    title = models.CharField(max_length=128)
    nickname = models.CharField(max_length=50, unique=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
