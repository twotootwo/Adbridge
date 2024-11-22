from django.contrib import admin

from logg.models import User, Profile


# Register your models here.
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password','position')
    pass
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','position')