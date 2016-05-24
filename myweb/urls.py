"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ourlove import views
from english import views as eng_view
from article import views as art_view

urlpatterns = [
    url(r'^article/(\d)$', art_view.article, name='article'),
    url(r'^article/write$', art_view.write, name='to_write'),
    url(r'^article/add', art_view.add, name='add_article'),
    url(r'^english/index$', eng_view.index),
    url(r'^english/translate/([a-zA-Z]+)', eng_view.translate_word, name='translate'),
    url(r'^english/translate$', eng_view.translate),
    url(r'^$', views.index, name='home'),
    url(r'^admin/', admin.site.urls),
]
