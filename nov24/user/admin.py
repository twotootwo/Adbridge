from django.contrib import admin

from user.models import CustomUser, InfluencerProfile, AdvertiserProfile

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(InfluencerProfile)
admin.site.register(AdvertiserProfile)