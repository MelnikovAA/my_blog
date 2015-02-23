from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Article, Comment


# Create your views here.
def all_articles(request):
	
	articles = Article.objects.all()
	comments_count = {}
	
	for article in articles:		
		comments_count[article.id] = Comment.objects.filter(article_key = article.id).count()
	
	return render_to_response('main.html',{'articles': articles, 'comments':comments_count})
	
def article_read(request,article_id = 1):
	try:
		art = Article.objects.get(id = article_id)
	except Exception:
		art = Article.objects.get(id = 1)
	return render_to_response('article.html',{'article':art, 'comments':Comment.objects.all()})


