from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
# 执行响应的代码所在模块

# 每个响应对应一个函数，函数必须返回一个响应
# 函数必须存在一个参数，一般约定为request
# 每个响应（函数）对应一个url
# def index(request):
#     return HttpResponse("Hellow world!")

# render()函数中支持一个dict类型参数
# 该字典是后台传递到模板的参数，键为参数名
# 在模板中使用{{参数名}}来直接使用
def index(request):
    articles = models.Article.objects.all()
    return  render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id','0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})
