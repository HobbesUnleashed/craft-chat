from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = "desription"


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "category", "age", "skill", "created_on")
    search_fields = ["title", "category"]
    list_filter = ("category",)
    summernote_fields = ("content", "materials")


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ("post", "content", "created_on")
    search_fields = ["content", "post"]
    summernote_fields = ("content",)
