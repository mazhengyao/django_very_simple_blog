from django.db import models

# Create your models here.
# 通常，一个model对应数据库的一张数据表
# Django中的models以类的形式表现
# 它包含一些基本的字段以及数据的一些行为
# ORM 对象关系映射
# 实现了对象和数据库之间的映射
# 隐藏了数据访问的细节，不需要编写sql语句
# 在应用根目录下创建models.py，并引入models模块
# 创建类，继承models.Model，该类即是一张数据表
# 在类中创建字段
# 字段即类里面的属性（变量）
# 生成数据表 manage.py同级目录
# 执行 python manage.py makemigrations app名（可选）
# 再执行python manage.py migrate
# Django会自动在app/migrations/目录下生成移植文件
# 执行python manage.py sqlmigrate 应用名 文件id（000001...） 查看sql语句
# 默认sqlite3 在db.sqlite3

class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title