from django.contrib import admin

from mainapp import models


class CategoryAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['slug'].required = False
        return form


class ProductAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(ProductAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['slug'].required = False
        return form


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
# admin.site.register(models.Cart, admin.ModelAdmin)
