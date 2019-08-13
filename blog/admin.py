from django.contrib import admin

from blog.models import  Article

# Register your models here.
# 该应用的后台管理系统配置
# 自动化数据管理界面，被授权的用户可直接在admin中管理数据库
# django提供了许多针对admin的定制功能
# 创建用户 python manage.py createsuperuser

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)

admin.site.register(Article, ArticleAdmin)