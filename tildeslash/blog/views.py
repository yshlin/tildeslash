from django.core.paginator import Paginator
from django.shortcuts import render

import commonware
from tildeslash.blog.models import Post
from tildeslash.settings import POSTS_PER_PAGE


log = commonware.log.getLogger('blog')


def home(request):
    return paged_posts(request)


def paged_posts(request, page=1):
    posts = Post.objects.filter(status='published').order_by('-publish_time')
    p = Paginator(posts, POSTS_PER_PAGE).page(page)
    data = {'posts': p.object_list, 'pager': p}
    return render(request, 'blog/home.html', data)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    data = {'post': post}
    return render(request, 'blog/post.html', data)


def tagged_posts(request, slug, page=1):
    posts = Post.objects.filter(tags__name__in=[slug, ]).order_by('-publish_time')
    p = Paginator(posts, POSTS_PER_PAGE).page(page)
    data = {'tag': slug, 'posts': p.object_list, 'pager': p}
    return render(request, 'blog/tagged-posts.html', data)
