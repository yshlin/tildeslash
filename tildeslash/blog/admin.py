from functools import update_wrapper
from django.contrib.admin import ModelAdmin
from django.contrib.admin.util import unquote
from django.forms.models import ModelForm
from django_ace import AceWidget
from django.contrib import admin
from django.shortcuts import render
from tildeslash.blog.models import Post


class PostAdminForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content': AceWidget(mode='markdown', theme='twilight', width='800px', height='600px'),
        }


class PostAdmin(ModelAdmin):
    form = PostAdminForm
    change_form_template = 'admin/custom_post_change_form.html'

    def get_urls(self):
        from django.conf.urls import patterns, url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)
        urls = super(PostAdmin, self).get_urls()
        my_urls = patterns(
            '',
            url(r'^(?P<post_id>\d+)/preview/$',
                wrap(self.preview_post),
                name='post.preview'),
        )
        return my_urls + urls

    def preview_post(self, request, post_id, extra_context=None):
        print post_id
        post = self.get_object(request, unquote(post_id))
        data = {
            'post': post,
        }
        return render(request, 'blog/post.html', data)



admin.site.register(Post, PostAdmin)