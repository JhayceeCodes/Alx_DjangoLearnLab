"""from django.contrib import admin
from .models import Book, CustomUser, CustomUserAdmin

@admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)


@admin.site.register(CustomUser, CustomUserAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "date_of_birth")
"""