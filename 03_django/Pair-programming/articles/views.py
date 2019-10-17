from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = ArticleForm(instance=article)
    comment_form = CommentForm()
    context = {'form': form, 'article':article, 'comment_form':comment_form}
    return render(request, 'articles/detail.html', context)

@require_http_methods("POST")
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance=article)
        context ={'form': form, 'article':article}
        return render(request, 'articles/form.html', context)

@require_http_methods("POST")
def comment_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    comment = comment_form.save(commit=False)
    # embed()
    comment.article_id = article_pk
    comment.save()
    return redirect('articles:detail', article_pk)

@require_http_methods("POST")
def comment_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = article.comments.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    