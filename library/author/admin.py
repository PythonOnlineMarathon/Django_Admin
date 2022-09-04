from django.contrib import admin

from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'surname', 'patronymic', ('date_of_birth','date_of_death'),'books']
    readonly_fields = ['id']
    list_display = ['id', 'name', 'surname', 'patronymic', ]
    list_display_links = ['id', 'name']
    search_fields = ['surname', 'books']
    # list_editable = ('is_published',)
    list_filter = ['surname', 'books']
    list_select_related = True

admin.site.register(Author, AuthorAdmin)

