from django.contrib import admin

from logg.models import User


# Register your models here.
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password','position')
    pass