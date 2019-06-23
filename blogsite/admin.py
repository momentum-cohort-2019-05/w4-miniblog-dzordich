from django.contrib import admin

from blogsite.models import Blogger, BlogPost, Comment

# Register your models here.
admin.site.register(Comment)

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'post_date')
    inlines = [CommentInline]


class BlogPostInline(admin.TabularInline):
    model = BlogPost
    extra = 0

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    inlines = [BlogPostInline]