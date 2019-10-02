# Django 4

어제 했던거.

```python
$ python manage.py shell
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from articles.models import Article
>>> Article.objects.all()
<QuerySet [<Article: 1번글 - first: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - fourth: django!>, <Article: 5번글 - first: hahaha>, <Article: 6번글 - first: vacation>]>
>>> articles = Article.objects.all()
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - fourth: django!>, <Article: 5번글 - first: hahaha>, <Article: 6번글 - first: vacation>]>
```

1번째 가져오기

```
>>> Article.objects.get(pk=1)
<Article: 1번글 - first: django!>
>>> article = Article.objects.get(pk=1)
>>> type(article)
<class 'articles.models.Article'>
```

타입에 주목

```
>>> article = Article.objects.get(pk=1)
>>> type(article)
<class 'articles.models.Article'>
>>> article = Article.objects.filter(pk=1)
>>> type(article)
<class 'django.db.models.query.QuerySet'>
```

. get했을때랑 filter랑 타입이 다름.

.get은 하나만 있다고 상정하고 가져오고  filter 은 몇 개 가져올지 모르는 거라 타입이 다름



.get과 .filter의 차이를 숙지할 것.

```python
>>> type(article)
<class 'django.db.models.query.QuerySet'>
>>> article.id
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'id'
>>> article = Article.objects.get(pk=1)
>>> article.id
1
>>> article.content
'django!'
```





##### order_by

```html
>>> articles = Article.objects.order_by('id')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - fourth: django!>, <Article: 5번글 - first: hahaha>, <Article: 6번글 - first: vacation>]>
>>> articles = Article.objects.order_by('-id')
>>> articles
<QuerySet [<Article: 6번글 - first: vacation>, <Article: 5번글 - first: hahaha>, <Article: 4번글 - fourth: django!>, <Article: 3번글 - third: django!>, <Article: 2번글 - second: django!>, <Article: 1번글 - first: django!>]>
```



인덱싱 해보기 

```
>>> article = Article.objects.all()[2]
>>> article
<Article: 3번글 - third: django!>
>>> type(article)
<class 'articles.models.Article'>
>>> article.id
3
```

속성접근이 가능

이현우 너 차이 알겠지?

ㅇㅇ

```
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - fourth: django!>, <Article: 5번글 - first: hahaha>, <Article: 6번글 - first: vacation>]>
>>> article
<Article: 3번글 - third: django!>
```





#### 슬라이싱

```
>>> articles = Article.objects.all()[1:3]
>>> articles
<QuerySet [<Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>]>

>>> article = articles[1]
>>> article
<Article: 3번글 - third: django!>
```





#### 포함된거 가져오기

```
>>> articles = Article.objects.filter(title__contains = 'fir')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 5번글 - first: hahaha>, <Article: 6번글 - first: vacation>]>
```

title에 fir이 포함된 걸 가져옴



```
>>> articles = Article.objects.filter(title__startswith='first')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 5번글 - first: hahaha>, <Article: 6번글 - first: vacation>]>
```

이건  title이 first로 시작하는 애들 가져옴



```
>>> articles = Article.objects.filter(content__endswith='!')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - fourth: django!>]>\
```

content 에 !로 끝나는 애들을 가져옴





```
>>> articles = Article.objects.filter(content__endswith='!')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - fourth: django!>]>
>>> articles[0]
<Article: 1번글 - first: django!>
>>> article = articles[0]
>>> article.id
1
```

쿼리셋에서 저렇게 하나만 가져오면 속성으로 접근 가능





#### 덮어쓰기

```
>>> article = Article.objects.get(pk=1)
>>> article
<Article: 1번글 - first: django!>
>>> article.title = 'byebye'
>>> article.save()
>>> article
<Article: 1번글 - byebye: django!>
```

save 필수.



#### 지우기

```
>>> article.delete()
(1, {'articles.Article': 1})
>>> Article.objects.get(pk=1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_django\02_django_query\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\TIL\03_django\02_django_query\venv\lib\site-packages\django\db\models\query.py", line 408, in get
    self.model._meta.object_name
articles.models.Article.DoesNotExist: Article matching query does not exist.
>>>
```

이건 세이브 안해도 됨



#### 종료

```
exit()
```







### 관리자 설정

```
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'student'): admin
이메일 주소:
Password:
Password (again):
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 너무 일상적인 단어입니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(venv)
```

비번은 쳐도 안보임



로그인

서버 실행시키고

주소 뒤에 admin/  ㄱ

``http://127.0.0.1:8000/admin/``

그럼 로그인 페이지 뜸 - 로그인 ㄱ





#### admin.py

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)


```





```python
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
```





### 추가확장툴

``$ pip install django-extensions``

등록도 해줘야함.

프로젝트에서 setting.py 에서 인스톨드 앱스 ㄱ

```

INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions'
]

```



```
$ python manage.py shell_plus
# Shell Plus Model Imports
from articles.models import Article
```

지 알아서 임포트하고 다 해줌

```
>>> article = Article.objects.get(pk=2)
>>> article
<Article: 2번글 - second: django!>
```

바로 쳐주면 됨



입력 복습 ㄱ

```
>>> article = Article()
>>> article.title = 'haha'
>>> article.content = 'hoho'
>>> article.save()
>>> article = Article(title = 'hahaha', content = 'hohoho')
>>> article.save()
>>> Article.objects.create(title='hahahaha', content = 'hhohohohoho')
<Article: 10번글 - hahahaha: hhohohohoho>
>>>
```

