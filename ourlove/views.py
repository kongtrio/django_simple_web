# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from article.models import Article


def index(request):
    articles = Article.objects.order_by("-alter_time").filter(display=True)[:5]
    return render(request, 'index.html', {"articles": articles})



