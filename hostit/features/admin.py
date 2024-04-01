from django.contrib import admin
from features.models import services
class serviceAdmin(admin.ModelAdmin) :
    list_display=['icon', 'tittle','description']

admin.site.register(services,serviceAdmin)

# Register your models here.
