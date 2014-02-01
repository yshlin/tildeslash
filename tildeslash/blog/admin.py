from django.contrib.admin import ModelAdmin
from django.forms.models import ModelForm
from django_ace import AceWidget
from django.contrib import admin
from tildeslash.blog.models import Post


class PostAdminForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content': AceWidget(mode='markdown', theme='twilight', width='800px', height='600px'),
        }


class PostAdmin(ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)