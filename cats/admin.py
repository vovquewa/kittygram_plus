from django.contrib import admin

from .models import Cat, Achievement  # , Owner


class CatAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'owner')
    empty_value_display = '-пусто-'


admin.site.register(Cat, CatAdmin)


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    empty_value_display = '-пусто-'


admin.site.register(Achievement, AchievementAdmin)
