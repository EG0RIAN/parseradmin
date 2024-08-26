from django.contrib import admin
from .models import ProductImage, Product


admin.site.register(ProductImage)
admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('brand',)