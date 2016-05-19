# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from util import date_util


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html', {"loveDays": date_util.today_to_loveday_days()})


def article(request):
    return render(request, 'article.html', {"loveDays": date_util.today_to_loveday_days()})
