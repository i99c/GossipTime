from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'updated_date', 'is_published')
    list_filter = ('is_published', 'created_date', 'updated_date')
    search_fields = ('title', 'content')
    readonly_fields = ('created_date', 'updated_date')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # İhtiyaca göre diğer alanlar eklenmeli

admin.site.register(Post, PostAdmin)
