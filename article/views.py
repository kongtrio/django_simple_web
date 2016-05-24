from django.shortcuts import render
from .models import Article
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.

def article(request, id):
    article = Article.objects.get(id=id)
    article.read_num += 1
    article.save()
    return render(request, 'article/article.html', {'article': article})


def write(request):
    return render(request, 'article/write_article.html')


def add(request):
    title = request.POST.get("title", "")
    images = request.POST.get("images", "/static/images/art_default.png")
    content = request.POST.get("content", "")
    author = request.POST.get("author", "")
    if title == '' or content == '' or author == '':
        return HttpResponseRedirect(reverse('home'))
    if images == '':
        images = "/static/images/art_default.png"
    article = Article(title=title, image=images, content=content, author=author)
    article.save()
    return HttpResponseRedirect(reverse('home'))
