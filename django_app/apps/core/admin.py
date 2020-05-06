from django.contrib import admin
from .models import Book, Author, Subscriber, Language


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_select_related = ('language',)
    list_display = ('title', 'language', 'publish_year', 'id')
    search_fields = ('title', 'publish_year')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'id')
    search_fields = ('last_name', 'first_name', 'middle_name')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'email', 'id')
    search_fields = ('last_name', 'first_name', 'middle_name')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'id')
    search_fields = ('name', 'code')
    ordering = ('name', 'code')
