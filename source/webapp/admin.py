from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from webapp.models import UserInfo, Post


class UserInfoInline(admin.StackedInline):
    model = UserInfo
    filter_horizontal = ('friend', )


class UserInfoAdmin(UserAdmin):
    inlines = [UserInfoInline]


admin.site.unregister(User)
admin.site.register(User, UserInfoAdmin)
# admin.site.register(UserInfo)
admin.site.register(Post)
