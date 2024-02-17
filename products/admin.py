from django.contrib import admin
from .models import Product, Category, ScentProfile

# Models

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'price',
        'scent_profile',
        'image',
    )

    ordering = ('sku',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "scent_profile":
            queryset = ScentProfile.objects.all()
            kwargs["queryset"] = queryset
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
