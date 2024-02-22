from django.contrib import admin
from .models import ScentProfile


class ScentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )


admin.site.register(ScentProfile, ScentProfileAdmin)
