from django.contrib import admin
from . import models

class ImageInline(admin.TabularInline):
  model = models.ItemImage
  
class ItemAdmin(admin.ModelAdmin):
  inlines = [
    ImageInline
  ]

admin.site.register(models.PlasticType)
admin.site.register(models.Category)
admin.site.register(models.Item)
admin.site.register(models.ItemImage)
admin.site.register(models.Store)
