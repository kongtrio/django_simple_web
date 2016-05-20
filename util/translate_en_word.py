# -*- coding=utf-8 -*-
from HTMLParser import HTMLParser
import urllib2
import re


# html解析器
class TranslationHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.word = []
        self.more_word = []
        self.opposites_word = []
        self.spell = []
        self.sentence = []
        self.div = None
        self.strong = None
        self.span = None
        self.div_num = 0
        self.div_now_num = -1

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            self.div_num += 1
            for (attr, value) in attrs:
                if attr == "class" and value == "basic clearfix":
                    self.div = "wordDiv"
                    self.div_now_num = self.div_num
                if attr == "class" and value == "phonetic":
                    self.div = "spellDiv"
                if attr == "class" and value == "section sent":
                    self.div = "sentence_div"
                if attr == "class" and value == "shape":
                    self.div = "more_word_div"
                if attr == "class" and value == "layout sort" and self.div == "sentence_div":
                    self.div_now_num = self.div_num
                    self.div = "sentence"
                if attr == "class" and "layout nf" in value:
                    self.div_now_num = self.div_num
                    self.div = "opposites_word"

        if tag == "strong":
            self.strong = "strong"
        if tag == "span":
            self.span = "span"

    def handle_endtag(self, tag):
        if tag == 'div':
            if self.div_num == self.div_now_num:
                self.div = None
                self.div_now_num = -1
            self.div_num -= 1
        if tag == 'strong':
            self.strong = None
        if tag == 'span':
            self.span = None

    def handle_data(self, data):
        # 获取单词解释
        if (self.span == "span" or self.strong == "strong") and self.div == "wordDiv":
            self.word.append(data)
        # 获取读音
        if self.span == "span" and self.div == "spellDiv":
            self.spell.append(data)
        # 获取例句
        if self.div == "sentence":
            self.sentence.append(data)
        # 获取更多关联词
        if self.div == "more_word_div" and self.span == "span":
            self.more_word.append(data)
        # 获取正反义词
        if self.div == "opposites_word":
            self.opposites_word.append(data)


# 翻译获取对应单词
class TranslateUtil(object):
    def list_to_trim_string(self, data_list):
        all_data = ""
        for data in data_list:
            if self.trim_and_encode(data) != "":
                all_data = all_data + self.trim_and_encode(data) + "\n"
        return all_data

    @staticmethod
    def trim_and_encode(value):
        space_pattern = re.compile("^\s+$")
        if space_pattern.match(value) is not None:
            return "".encode("utf-8")
        if value is None:
            return "".encode("utf-8")
        pattern = re.compile("[.\n]+")
        value = re.sub(pattern, "", value)
        return value.encode("utf-8")

    def tranlate_word(self, word):
        content = urllib2.urlopen("http://dict.cn/" + word).read()
        hp = TranslationHTMLParser()
        hp.feed(content.decode('utf-8'))
        hp.close()
        all_spell = self.list_to_trim_string(hp.spell)
        all_word = self.list_to_trim_string(hp.word)
        all_sent = self.list_to_trim_string(hp.sentence)
        all_more_word = self.list_to_trim_string(hp.more_word)
        all_opposites_word = self.list_to_trim_string(hp.opposites_word)
        if all_word == '':
            return []
        return all_word, all_spell, all_sent, all_more_word, all_opposites_word


if __name__ == '__main__':
    translate_util = TranslateUtil()
    result = translate_util.tranlate_word("dddd")
    print result
    for x in result:
        print x.decode("utf-8")
        print "------------"
