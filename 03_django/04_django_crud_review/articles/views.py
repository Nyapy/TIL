from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article
from IPython import embed

# Create your views here.

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by("-pk")
    # print(articles)
    # print(type(articles))
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)


def create(request):
    #포스트 요청일 때
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content= content)
        article.save()
        return redirect('articles:detail', article.pk)

    #겟 요청일 때
    else:
        return render(request, 'articles/create.html')
    # title = request.POST.get('title')
    # print(title)
    # content = request.POST.get('content')
    
    # #1. 첫번째 방법
    # # article = Article()
    # # article.title = title
    # # article.content = content
    # # article.save()

    # #2. 두번째 방법
    # article = Article(title=title, content = content)
    # article.save()

    # #3. 세번째 방법
    # # Article.objects.create(title=title, content=content)


    # return redirect(f'/articles/{article.pk}')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article':article }
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)

    else:
        context = {'article':article }
        return render(request, 'articles/update.html', context)