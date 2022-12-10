from django.contrib import admin
from blog.models import Tag, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
