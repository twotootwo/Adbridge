from django.db import models

class Video(models.Model):
    channel_id = models.CharField(max_length=255)  # 영상 제목
    youtube_url = models.URLField(max_length=200, verbose_name="YouTube URL")

    def __str__(self):
        return self.channel_id
