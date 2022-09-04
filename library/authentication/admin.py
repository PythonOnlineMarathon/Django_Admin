from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'middle_name', 'created_at', 'updated_at', 'role', 'is_active')
    list_display_links = ('id', 'email')
    search_fields = ('first_name', 'last_name','email','role', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'role')


admin.site.register(CustomUser, CustomUserAdmin)

