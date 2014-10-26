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

class Tag(models.Model):
	name = models.CharField(max_length=200)
	article = models.ForeignKey(Article)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		tg = self.name
		art = self.article.title
		nm = tg + ": " + art
		return nm