import re

import markdown
from markdown.extensions.toc import TocExtension

from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .models import Article, Category, Tag


def index(request):
    article = Article.objects.all()
    return render(request, 'blog/index.html', context={
        "post_list": article
    })


def detail(request, pk):
    post = get_object_or_404(Article, id=pk)

    # 文章主题支持markdown格式
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            TocExtension(slugify=slugify),
        ])
    # 通过markdown 格式自动生成目录
    post.body = md.convert(post.body)

    # 当md.toc没有目录结构式显示为空
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/single.html', context={'post': post})


def archive(request, year, month):
    post_list = Article.objects.filter(create_time__year=year,
                                       create_time__month=month
                                       ).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Article.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Article.objects.filter(tags=t).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
