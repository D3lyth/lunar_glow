from django.contrib import admin
from .models import ProductScent, ScentProfile


class ScentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )

class ProductScentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'scentoptions',
    )

admin.site.register(ProductScent, ProductScentAdmin)
admin.site.register(ScentProfile, ScentProfileAdmin)
