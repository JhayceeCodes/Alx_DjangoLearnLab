from django.contrib import admin
from .models import Book, CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)


class CustomUserAdmin(admin.ModelAdmin):
    list_display =("first_name", "last_name")

admin.site.register(CustomUser, CustomUserAdmin)
