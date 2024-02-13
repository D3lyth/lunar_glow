from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'timestamp')
    search_fields = ('email', 'name')
    list_filter = ('timestamp',)

# Register the Subscriber model with the admin site
admin.site.register(Subscriber, SubscriberAdmin)
