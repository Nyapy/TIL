from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
import hashlib
from IPython import embed


def index(request):
    # embed()

    #1. session 정보에서 visits_num 이라는 키로 접근해 값을 가져옴
    #해당하는 키가 없으면 0을 가져옴
    visits_num = request.session.get('visits_num', 0)

    #2. 가져온 값을 session에 'visits_num'이라는 새로운 키의 값으로 1씩 증가
    request.session['visits_num'] = visits_num +1

    #3. session data를 수정하면 장고는 수정한 내용을 알 수 없어서 작성하는 코드
    request.session.modified = True

    articles = Article.objects.all()
    context = {'articles': articles, 'visits_num':visits_num,}
    # embed()
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    """
    Form Class
    모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 데이터 정제 후 DB에 실제 저장하는 로직 필요
    
    Model Form
    이미 Model에 대한 정보(스키마)를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지 알고 있음.
    form.save()만 해도 DB에 저장됨
    """
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        #해당 폼이 유효한지 확인
        if form.is_valid():
            article = form.save(commit=False)
            article.user_id = request.user.id
            # embed()
            article.save()
            # # form.cleaned_data를 통해 폼 데이터를 정제한다.(form.cleand_data -> Dict)
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content = content) # .create(.save() X)
            # embed()

            #1. content를 기준으로 리스트를 변경 후 for 문
            for word in article.content.split():
                #2 '#'으로 시작하는 요소를 선택
                if word.startswith('#'):
                    #3. word랑 같은 해시태그를 찾고 있으면 
                    # 기존 객체가 없으면 새로운 객체 생성
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    #4. 게시글의 해시태그 목록에 해당 단어를 추가
                    article.hashtags.add(hashtag)
            return redirect('articles:detail', article.pk)
        
        # title = request.POST.get('title')
        #     content = request.POST.get('content')
        #     article = Article(title=title, content = content)
        #     article.save() # .create(.save() X)

        return redirect('articles:detail', article.pk )
    
    else:
        form = ArticleForm()
        # embed()
        
    context = {'form': form,}
    return render(request, 'articles/form.html', context )

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comments.all()
    person = get_object_or_404(get_user_model(), pk=article.user.pk)
    context = {
        'article':article, 
        'comment_form': comment_form, 
        'comments': comments,
        'person' : person,
        }
    return render(request, 'articles/detail.html', context)

# @login_required
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.user == request.user:
            article.delete()
    return redirect('articles:index')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user :
        if request.method == 'POST':
            # instance - > 수정의 대상이 되는 특정한 글 객체
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                article.hashtags.clear()
                for word in article.content.split():
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                # embed()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article.pk)

    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)



"""
*CREATE & UPDATE는 같은
Create 로직
1.GET
- 사용자가 데이터를 입력할 수 있는 빈 Form을 제공
2.POST
- 사용자가 보낸 새로운 글을 DB에 저장

Update 로직
1.GET
- 기존 사용자의 글이 입력된 Form 제공
2.POST
- 수정된 글을 DB에 저장
"""

# @login_required
@require_POST
def comment_create(request, article_pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article_id = article_pk
            comment.save()
        if request.user == comment.user:
            return redirect('articles:detail', article_pk)
    return redirect('articles:detail', article_pk)


# @login_required
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    # 해당 게시글에 좋아요를 누른 사람들 중에서 user.pk(현재 요청 유저)를 가진 user가 존재하면
    if article.like_users.filter(pk=user.pk).exists():
        # 좋아요 취소
        article.like_users.remove(user)
    # 존재하지 않는 다면 좋아요를 누른 유저 목록에 유저 추가
    else:
        # 좋아요 누름
        article.like_users.add(user)
    return redirect('articles:index')


@login_required
def follow(request, article_pk, user_pk):
    # 게시글을 작성한 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 접속 유저(해당 함수로 요청을 보낸 사람)
    user = request.user

    #해당 person의 팔로워 중에서 이 함수를 요청한 유저가 존재하면
    if person.followers.filter(pk=user.pk).exists():
        # 언팔로우
        person.followers.remove(user)
    else:
        # 팔로우
        person.followers.add(user)
    return redirect('articles:detail', article_pk)

@login_required
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)

    articles = hashtag.article_set.order_by('-pk')
    context = {'hashtag':hashtag, 'articles':articles, }
    return render(request, 'articles/hashtag.html', context)