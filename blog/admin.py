from django.contrib import admin
from .models import Blog, BlogComment, BlogCategory


# Register your models here.

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_time', 'category', 'content')


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog', 'pub_time', 'content')


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
