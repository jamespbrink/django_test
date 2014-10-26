from django import template
from article.models import Tag

register = template.Library()

def tags_list():
	list = Tag.objects.values('name').distinct()
	return {'list': list}

register.inclusion_tag('tags_template.html')(tags_list)