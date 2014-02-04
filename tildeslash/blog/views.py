from django.shortcuts import render

import commonware
from tildeslash.blog.models import Post


log = commonware.log.getLogger('blog')


def home(request):
    """Main example view."""
    posts = Post.objects.filter(status='published')
    data = {'posts': posts}  # You'd add data here that you're sending to the template.
    return render(request, 'blog/home.html', data)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    data = {'post': post}
    return render(request, 'blog/post.html', data)


def tagged_posts(request, slug):
    posts = Post.objects.filter(tags__name__in=[slug, ])
    data = {'tag': slug, 'posts': posts}
    return render(request, 'blog/tagged-posts.html', data)
