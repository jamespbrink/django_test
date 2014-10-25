from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	name = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	article = models.ForeignKey(Article)
	approved = models.BooleanField(default='False')
	code = models.CharField(max_length=15)

	def __unicode__(self):
		bod = self.body[:25]
		com = self.article.title + " - " + self.name + ": " + bod
		return com