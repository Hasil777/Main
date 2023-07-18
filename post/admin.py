from django.contrib import admin
from .models import Post,Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-id']
    search_fields = ['name']
    prepopulated_fields={
        'slug':('name',)
    }
    date_hierarchy = 'publish'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','post','created','active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name']