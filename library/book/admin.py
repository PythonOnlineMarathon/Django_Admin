from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    def author_names(self,obj):
        return u" %s" % (u", ".join([author.full_name for author in obj.authors.all()]))
    author_names.short_description='Authors'
    
    # fields = ['id', 'name', 'description', 'year_publish', 'count', 'year_issue','authors']
    readonly_fields = ['id']
    list_display = ['id', 'name', ]
    list_display_links = ['id', 'name']
    search_fields = ['name', 'description', 'authors__surname']
    list_filter = ['name', 'year_publish']
    list_select_related = True

admin.site.register(Book, BookAdmin)



