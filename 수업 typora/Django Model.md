database/SQL



database

스키마(scheme)

데이터 베이스의 구조와 제약조건(자료구조, 표현방법, 관계)에 관한 전반적 명세를 기술한 것.

기본키 : 각 행(레코드)고유값으로 Primary Key로 불린다. 반드시 설정되어야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용됨.



SQL(Structured Query Language) : Database와 Code를 연결함

INSERT, DELETE, UPDATE, SELECT

CRUD

CREATE,DELETE, UPDATE, READ



ORM: SQL문을 쓰지 않고 코드를 연결하게 만들어줌



id, title, content, created_at, updated_at





### Model

만들어진 앱에서 models.py에서 

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```



그 후

python manage.py makemigrations

하면 새로 migrations가 만들어짐. 안에 0001 파일이 있음

아직 데이터베이스에 반영되지 않은 상태임 여기는

그런데 다시 models.py에서 수정해서

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) ##시험나올 것 같음
    updated_at = models.DateTimeField(auto_now=True)
```

이렇게 updated_at을 추가해서 만들어주고

다시 python manage.py makemigrations를 해주면

migrations에 0002 파일이 만들어짐



할 거 다하고

python manage.py migrate 하면

db.sqlite3 만들어짐

그냥보면 이상하게 보이고 sqlite를 설치해서

sqlite open database 하면 왼쪽 밑에 생김.



즉

1. models.py로  테이블을 작성
2. makemigrations를 통해 설계도를 작성
3. migrate로 생성





장고 쉘 사용

python mange.py shell을 사용해서 쟝고 쉘 사용

거기에 

``from articles.models import Article``

``Article.objects.all()`` = 번역기같은 거임



#### 내용쓰기

``article = Article()`` 인스턴스 생성

``article.title= 'first'``

``article.content = 'django!' ``

``article.save()`` 저장

첫번째 방법

```bash
>>> article = Article()
>>> article.title = 'first'
>>> article.content = 'django!'
>>> article
<Article: Article object (None)>
>>> article.save()
>>> article
<Article: Article object (1)>
>>> article.title
'first'
>>> article.content
'django!'
>>> article.created_at
datetime.datetime(2019, 8, 7, 7, 9, 46, 388459, tzinfo=<UTC>)
```

두 번째 방법

```python
>>> article = Article(title='second', content = 'django!')
>>> article
<Article: Article object (None)>
>>> article.save()
>>> article
<Article: Article object (2)>
```

``Article.objects.get(pk=1)`` 하면 처음 걸로 접근 가능

전체를 보고 싶으면 

```python
>>> articles = Article.objects.all()
>>> articles
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
```



세 번째 방법

```python
>>> Article.objects.create(title='third', content='django!')
<Article: Article object (3)>
```

이건 바로 저장됨.

```
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
>>>
```

이렇게 전체 확인 가능





```
>>> article = Article()
>>> article.title = 'fourth'
>>> article.content = 'django!'
>>> article.title
'fourth'
>>> article.id
>>> article.save()
>>> article.id
4
```

save 메서드를 쓰기 전엔 id가 배정이 안되는 걸 볼 수 있음



```
>>> article = Article()
>>> article.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_django\02_django_query\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 필드는 빈 칸으로 둘 수 없습니다.'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
>>> article.title = 'Nyapy nyapy genius Nyapy'
>>> article.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_django\02_django_query\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 24 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
>>>
```

full_clean으로 다 지울 수 있는데 타이틀을 빈칸으로 둘 수 없다고 난리침.  전체를 지우는 건 아니고 입력 중인 것만 지우나봄



다시 model.py를 수정

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) ##시험나올 것 같음
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'
```

터미널 킬 후 다시 실행

```bash
$ python manage.py shell
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from articles.models import Article
>>> articles = Article.objects.all()
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - fourth: django!>]>
>>> type(articles)
<class 'django.db.models.query.QuerySet'>
>>>
```



필터

```
>>> Article.objects.create(title='first', content = 'hahaha')
<Article: 5번글 - first: hahaha>
>>> articles = Article.objects.filter(title='first')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 5번글 - first: hahaha>]>
>>>

```

와우. 이런 것도 됨.

```
<Article: 6번글 - first: vacation>
>>> article = Article.objects.filter(title='first').first()
>>> article
<Article: 1번글 - first: django!>
>>> article = Article.objects.filter(title='first').last()
>>> article
<Article: 6번글 - first: vacation>
```

.first()를 붙여서 처음 거를 부른 거임 second 이런건 안됨. 

퍼스트랑 라스트만 가능.



프라이머리키

```
>>> article = Article.objects.get(pk=1)
>>> article
<Article: 1번글 - first: django!>
```



.get은 고유한 값에만 써야됨 다른데 쓰면 이렇게 나옴

```
>>> article = Article.objects.get(title='first')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_django\02_django_query\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\TIL\03_django\02_django_query\venv\lib\site-packages\django\db\models\query.py", line 412, in get
    (self.model._meta.object_name, num)
articles.models.Article.MultipleObjectsReturned: get() returned more than one Article -- it returned 3!
```

first라는 타이틀이 3개라 일케 뜸

```
>>> article = Article.objects.get(pk=10)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_django\02_django_query\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\TIL\03_django\02_django_query\venv\lib\site-packages\django\db\models\query.py", line 408, in get
    self.model._meta.object_name
articles.models.Article.DoesNotExist: Article matching query does not exist.
>>>
```

없으면 이렇게 뜸

필터는 없으면 쿼리셋을 리턴해주는데 .get은 에러남

```
>>> article = Article.objects.filter(pk=10)
>>> article
<QuerySet []>
```

봐 빈 쿼리셋 들어간댔지.