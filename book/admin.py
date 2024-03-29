from django.contrib import admin
from book.models import Seria, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'serias')
    filter_horizontal = ('authors',)
 

admin.site.register(Seria)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)