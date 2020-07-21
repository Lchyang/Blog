from django.contrib import admin

from .models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    # list_display admin后台展示时的字段
    list_display = ['title', 'author',
                    'category', 'create_time', 'modify_time']
    # fields 后台创建操作时展示的字段
    fields = ['title', 'body', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# 将自定义的类注册进来
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
