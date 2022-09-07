from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Class adds bootstrap themed field for user content(temp doc)
    """
    list_filter = ('status', 'created_on')
    list_display = ('creator', 'created_on')
    search_fields = ['creator', 'user_text']
    summernote_fields = ('user_text')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    temp doc
    """
    list_filter = ('user_profile', 'approved', 'text', 'created_on')
    list_display = ('approved', 'created_on')
    search_fields = ['name', 'text']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
