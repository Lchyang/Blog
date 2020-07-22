import re

import markdown
from markdown.extensions.toc import TocExtension

from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .models import Article




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
