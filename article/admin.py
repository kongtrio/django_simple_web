from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'public_time', 'alter_time', 'read_num')


admin.site.register(Article, ArticleAdmin)
