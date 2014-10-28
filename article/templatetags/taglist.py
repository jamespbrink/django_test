from django import template
from article.models import Tag

register = template.Library()

@register.inclusion_tag('tags_template.html')
def list_tags():
	list = Tag.objects.values('name').distinct()
	return {'list': list}

