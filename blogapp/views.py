import re

import markdown
from markdown.extensions.toc import TocExtension

from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView, DetailView

from .models import Article, Category, Tag


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = Article
    context_object_name = 'post'
    template_name = 'blog/single.html'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)

    # 文章阅读量
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
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
        return post



def archive(request, year, month):
    post_list = Article.objects.filter(create_time__year=year,
                                       create_time__month=month
                                       ).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Article.objects.filter(tags=t).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
