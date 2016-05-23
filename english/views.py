# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Word
from util import translate_en_word
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
    return render(request, 'en/index.html')


def translate(request):
    post_len = len(request.POST)
    if post_len == 0:
        return HttpResponseRedirect('/english/index')
    word = request.POST['word']
    return HttpResponseRedirect(reverse('translate', args={word: word}))


def translate_word(request, word):
    get_word = {}
    not_foutn = None
    if word is not None:
        word_list = Word.objects.filter(en_word=word)
        if get_word is None or len(word_list) == 0:
            translate_util = translate_en_word.TranslateUtil()
            result = translate_util.tranlate_word(word)
            if len(result) == 0:
                not_foutn = True
            else:
                db_word = Word(en_word=word, cn_word=result[0], en_spell=result[1], sentence=result[2],
                               more_word=result[3],
                               opposites_word=result[4])
                db_word.save()
                get_word = db_word
        else:
            get_word = word_list[0]
    return render(request, 'en/index.html', {'word': get_word, "not_found": not_foutn, 'search_word': word})
