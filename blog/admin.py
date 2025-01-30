from django.contrib import admin
from blog.models import Author, Blog, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    fields = ['name','surname']
    list_display = ['name','surname']
    search_fields = ['name','surname']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    model = Blog
    fields = ['title','content','author']
    list_display = ['title','content', 'date_publish']
    search_fields = ['title','content', 'date_publish']
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    fields = ['author', 'blog', 'content']
    list_display = ['author','content','date_publish']
    search_fields = ['author','content','date_publish']