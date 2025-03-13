from django.contrib import admin

from mainapp import models


admin.site.register(models.Category, admin.ModelAdmin)
admin.site.register(models.Product, admin.ModelAdmin)
admin.site.register(models.Cart, admin.ModelAdmin)
