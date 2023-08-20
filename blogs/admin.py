from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contained', 'preview_image', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'contained')
