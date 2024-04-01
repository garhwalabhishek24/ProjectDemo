from django.contrib import admin
from news.models import news

class newsAdmin(admin.ModelAdmin):
    list_display=('tittle','newdesc')

admin.site.register(news,newsAdmin)
# Register your models here.
