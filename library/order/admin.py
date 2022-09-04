from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', ('created_at', 'end_at', 'plated_end_at')]
    list_display_links = ['id', 'created_at']
    search_fields = ['created_at', 'user', 'book']
    list_filter = ['user', 'book']
    readonly_fields = ['id', 'created_at']



admin.site.register(Order, OrderAdmin)

