from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def index(request):
    article = Article.objects.all()
    return render(request, 'blog/index.html', context={
        "post_list": article
    })


def detail(request, pk):
    post = get_object_or_404(Article, id=pk)
    return render(request, 'blog/single.html', context={'post': post})
