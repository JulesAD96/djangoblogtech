from django.contrib import admin
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at', 'updated_at')
    list_filter = ['author']
    prepopulated_fields = {"slug":("title",)}
    
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body_comment', 'created_at')
    list_filter = ['author']
    
admin.site.register(Comment, CommentAdmin)
