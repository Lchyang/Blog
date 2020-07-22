from django.db import models
from django.utils import timezone

from blogapp.models import Article


class Comment(models.Model):
    name = models.CharField(verbose_name='名字', max_length=50)
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(verbose_name='网址', blank=True)
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    post = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])