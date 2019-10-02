# Django

Versatile Secure Scalable Complete Maintainable Potable



hotframeworks.com :  프레임웤 인기순위



MTV(모델 템플릿 뷰) 





## 장고 ㄱ

.gitignore 파일 만들고 

gitignore.io 가서 django 치고 .gitignore 파일에 넣을거 복붙 ㄱ



### 독립환경 실행시키기



```bash
student@DESKTOP MINGW64 ~/TIL/03_django (master)
$ mkdir 01_django_intro

student@DESKTOP MINGW64 ~/TIL/03_django (master)
$ cd 01_django_intro/

student@DESKTOP MINGW64 ~/TIL/03_django/01_django_intro (master)
$ python -m venv venv

student@DESKTOP MINGW64 ~/TIL/03_django/01_django_intro (master)
$ source venv/Scripts/activate
(venv)

student@DESKTOP MINGW64 ~/TIL/03_django/01_django_intro (master)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 19.2.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
(venv)
student@DESKTOP MINGW64 ~/TIL/03_django/01_django_intro (master)
$ deactivate

student@DESKTOP MINGW64 ~/TIL/03_django/01_django_intro (master)
$ source venv/Scripts/activate
(venv)
```



### Django 설치

```bash
$ pip install django
Collecting django
  Downloading https://files.pythonhosted.org/packages/d6/57/66997ca6ef17d2d0f0ebcd860bc6778095ffee04077ca8985928175da358/Django-2.2.4-py3-none-any.whl (7.5MB)
    100% |████████████████████████████████| 7.5MB 6.0MB/s
Collecting sqlparse (from django)
  Downloading https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
Collecting pytz (from django)
  Downloading https://files.pythonhosted.org/packages/87/76/46d697698a143e05f77bec5a526bf4e56a0be61d63425b68f4ba553b51f2/pytz-2019.2-py2.py3-none-any.whl (508kB)
    100% |████████████████████████████████| 512kB 20.5MB/s
Installing collected packages: sqlparse, pytz, django
Successfully installed django-2.2.4 pytz-2019.2 sqlparse-0.3.0
You are using pip version 19.0.3, however version 19.2.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
(venv)
student@DESKTOP MINGW64 ~/TIL/03_django/01_django_intro (master)
$ pip list
Package    Version
---------- -------
Django     2.2.4
pip        19.0.3
pytz       2019.2
setuptools 40.8.0
sqlparse   0.3.0
You are using pip version 19.0.3, however version 19.2.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
(venv)
```

pip list 찍으면 몇 개 안나옴



### 장고 프로젝트 ㄱ

```bash
django-admin startproject django_intro .
```

맨뒤에 . 안찍으면 폴더 하나 더 만들어짐.



#### 서버실행 

```bah
python manage.py runserver
```



#### 앱 생성

```
python manage.py startapp pages
```

```django-admin startapp pages``` 로 만들어도 되지만 좀 차이 있음. 뭔차이인지는 나중에 ㄱ



앱을 생성하면 출생신고 해줘야함.

프로젝트에 settings.py 에 들어가서 



```python
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

여기에 앱이름 추가해줌.



#### 날짜, 언어 바꾸기

같은 곳에서

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

#### templates 폴더 생성

```
생성한 앱폴더 아래 'templates' 폴더 생성
```





##### .py 3대장

models, views, urls



### urls.py

흡사 집배원



```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
```

index/를 요청하면 views.index   함수를 실행

views는 pages에 있으니 임포트 해줘야함.

##### views.py

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
```

이게 기본 골격



pages에 templates 폴더에

index.html 생성

```python
<h1>First Django App!</h1>
```



![](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564974980049.png)

실행 시켜서 뒤에 index/ 붙이면 이렇게 나옴.







### 템플릿 변수

```html
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

#2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ('족발', '햄버거', '피자', '초밥')
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

```

