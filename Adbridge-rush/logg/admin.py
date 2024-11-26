from django.contrib import admin

from logg.models import User, Advertisement


# Register your models here.
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password','position')
    pass
@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'min_budget', 'max_budget','product_image')
    pass