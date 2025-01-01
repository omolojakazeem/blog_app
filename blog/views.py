from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    template = 'post/list.html'
    
    return render(request, template_name=template, context=context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED) 
    context = {
        'post': post
    }
    template = 'post/detail.html'
    return render(request, template_name=template, context=context)