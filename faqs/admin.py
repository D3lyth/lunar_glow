from django.contrib import admin
from .models import FAQCategory, FAQ_QA

# Models


class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class FAQ_QAAdmin(admin.ModelAdmin):
    list_display = (
        'faq_category',
        'question',
        'answer',
        )


admin.site.register(FAQCategory, FAQCategoryAdmin)
admin.site.register(FAQ_QA, FAQ_QAAdmin)
