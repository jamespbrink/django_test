from django.contrib import admin
from article.models import Article
from article.models import Comment
from article.models import Tag

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)

# Register your models here.
