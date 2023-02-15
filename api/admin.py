from django.contrib import admin
# from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from . import models


# admin.site.register(Post)

class PostAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    body = forms.CharField(label="Статья", widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Post
        fields = '__all__'


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'created', 'categories')
    list_display_links = ('owner',)
    list_filter = ('created',)
    search_fields = ('title', 'categories__name')
    form = PostAdminForm


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'created')
    list_display_links = ('owner',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)



