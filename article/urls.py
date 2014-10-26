from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'article.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
	url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),
	url(r'^create/$', 'article.views.create'),
	url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
	url(r'^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
	url(r'^approvecom/(?P<comment_code>[^/]+)/$', 'article.views.approve_comment'),
	url(r'^deletecom/(?P<comment_code>[^/]+)/$', 'article.views.delete_comment'),
	url(r'^tags/(?P<tags>[^/]+)/$', 'article.views.tags'),
)