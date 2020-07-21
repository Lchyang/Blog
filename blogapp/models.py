from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Article(models.Model):
    """
    文章
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=100, verbose_name='文章标题')
    body = models.TextField(verbose_name='文章正文')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间')

    # 模板中调用model时生成一个具体的url，传递给前端，用户点击url时，传到views展示具体页面
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogapp:detail', kwargs={'pk':self.id})

    # 重写save方法保存每次修改时间
    def save(self, *args, **kwargs):
        self.modify_time = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
