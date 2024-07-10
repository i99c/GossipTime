from django.contrib import admin
from .models import Reader, Writer, Article, ArticleComment, UserLog

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_darkmode', 'is_delete', 'delete_date', 'created_date', 'updated_date', 'slug')
    list_filter = ('is_darkmode', 'is_delete', 'created_date', 'updated_date')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone')
    readonly_fields = ('created_date', 'updated_date', 'slug')

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_darkmode', 'is_delete', 'delete_date', 'created_date', 'updated_date', 'slug')
    list_filter = ('is_darkmode', 'is_delete', 'created_date', 'updated_date')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone')
    readonly_fields = ('created_date', 'updated_date', 'slug')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'is_delete', 'delete_date', 'created_date', 'updated_date', 'slug')
    list_filter = ('is_delete', 'created_date', 'updated_date')
    search_fields = ('title', 'writer__user__username', 'writer__user__first_name', 'writer__user__last_name')
    readonly_fields = ('created_date', 'updated_date', 'slug')

@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'reader', 'content', 'is_delete', 'delete_date', 'created_date')
    list_filter = ('is_delete', 'created_date')
    search_fields = ('article__title', 'reader__user__username', 'reader__user__first_name', 'reader__user__last_name')
    readonly_fields = ('created_date',)

@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'action')
    readonly_fields = ('created_date',)
