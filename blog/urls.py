from django.urls import path, re_path
from . import views

urlpatterns = [
    # 加斜杠
    path('index/', views.index),
    re_path(r'^article/(?P<article_id>[0-9]+)/$',views.article_page, name='article_page'),
    # path('article/<int:article_id>/', views.article_page, name='article_page'),
    re_path(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page, name='edit_page'),
    path('edit/action/', views.edit_action, name='edit_action'),

]