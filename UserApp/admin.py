from django.contrib import admin
from UserApp.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'image_tag']
    list_filter = ['user', ]


admin.site.register(UserProfile, UserProfileAdmin)
