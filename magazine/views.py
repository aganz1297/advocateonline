from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
# . signifies the current directory
from .models import Article, Issue

# Create your views here.
def index(request):
	all_articles = Article.objects.all()
	data = {
		'articles': all_articles,	
	}
	#template_name = 'index_v1.html',
	template_name = 'current_issues.html'
	return render_to_response(template_name, data, context_instance=RequestContext(request))

def article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	data = {
		'article': article
	}
	template_name = 'article.html'
	return render_to_response(template_name, data, context_instance=RequestContext(request))

def issues(request):
	all_issues = Issue.objects.all()

	data = {
		'issues': all_issues
	}
	template_name = 'issues.html'
	return render_to_response(template_name, data, context_instance=RequestContext(request))