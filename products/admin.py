from django.contrib import admin
from .models import Product, Category

# Models

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'price',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
