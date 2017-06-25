from django.contrib import admin
from products.models import *


class ProductImageInLine(admin.TabularInline): # привязывает картинки к товарам
    model = ProductImage
    extra = 0 # убирает лишние ряды

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInLine]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)