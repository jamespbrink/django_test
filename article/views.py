from django.shortcuts import render_to_response
from article.models import Article, Comment
from django.http import HttpResponse
from forms import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.utils.dateformat import format
from django.core.mail import send_mail
import random 
import string

def random_code(characters=string.ascii_letters+string.digits, length=5): 
    return ''.join( 
      random.choice(characters) 
      for _ in range(length) 
      ) 

# Create your views here.



def articles(request):
	language = 'en-us'
	session_language = 'en-us'

	if 'lang' in request.COOKIES:
		language  = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']

	return render_to_response('articles.html',
		{'articles': Article.objects.all(),
		'language': language,
		'session_language': session_language })

def article(request, article_id=1):
	return render_to_response('article.html',
		{'article': Article.objects.get(id=article_id) })

def language(request, language='en-us'):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang', language)
	request.session['lang'] = language
	return response

def create(request):
	if request.POST:
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/articles/all')
	else:
		form = ArticleForm()

	args = {}
	args.update(csrf(request))

	args['form'] = form

	return render_to_response('create_article.html', args)

def like_article(request, article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		count = a.likes
		count += 1
		a.likes = count
		a.save()
	return HttpResponseRedirect('/articles/get/%s' % article_id)

def add_comment(request, article_id):
	a = Article.objects.get(id=article_id)
	if request.method == "POST":
		f = CommentForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.pub_date = timezone.now()
			c.article = a
			c.approved = False
			codes = random_code() + format(timezone.now(), u'U')
			c.code = codes
			c.save()

			message = c.name + " commented on your article: " + c.article.title + "<br><br>" + c.body
			message = message + "<br><br>Follow this link to approve<br><a href='http://127.0.0.1/article/approvecom/" + codes + "/'>http://127.0.0.1/article/approvecom/" + codes + "</a><br><br>"
			message = message + "<br><br>Follow this link to delete<br><a href='http://127.0.0.1/article/approvecom/" + codes + "/'>http://127.0.0.1/article/deletecom/" + codes + "</a>"
			send_mail('Comment needs approval', message, 'admin@jamesbrink.net', ['james.p.brink@gmail.com'], fail_silently=False)

			return HttpResponseRedirect('/articles/get/%s' % article_id)

	else:
		f = CommentForm()

	args = {}
	args.update(csrf(request))

	args['article'] = a
	args['form'] = f

	return render_to_response('add_comment.html', args)

def approve_comment(request, comment_code):
	args = {}
	if comment_code:
		c = Comment.objects.get(code=comment_code)
		c.approved = True
		c.save()
		args['result'] = "success"
	else:
		args['result'] = "fail"
	return render_to_response('commentmod.html', args)

def delete_comment(request, comment_code):
	args = {}
	if comment_code:
		c = Comment.objects.get(code=comment_code)
		c.delete()
		args['result'] = "delete"
	else:
		args['result'] = "fail"
	return render_to_response('commentmod.html', args)






