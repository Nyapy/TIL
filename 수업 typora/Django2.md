# Django



### static 파일

App 폴더 아래 static 폴더를 만듬

static 폴더 아래 images와 stylesheets 폴더를 만듬

stylesheets 아래 style.css 파일을 만듬







## 다른앱(여러개 ) 만들기 ㄱ

urls.py 가 너무 길어지기 때문에

기존앱 아래 urls.py를 만들어주고  기존 프로젝트에서 했던 내용을 잘라서 붙여줌

```html
from django.urls import path
from . import views

urlpattuerns = [
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('ispal/<pal>', views.ispal),
    path('isbirth/', views.isbirth),
    path('student/<name>', views.student),
    path('info/', views.info),
    path('template_language/', views.template_language),
    path('area/<int:r>', views.area),
    path('mul/<int:num1>/<int:num2>', views.mul),
    path('I/<name>/<int:age>', views.I),
    path('hello/<str:name>/<int:age>/', views.hello), #디폴트가 str이라 str:은 지워도 무관
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
]
```



프로젝트 아래 urls.py는 이렇게 해줘야한다. 

from pages import view 는 지워줘도 됨

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pages/', include('pages.urls')), #pages의 url 파일을 포함해라.
    path('admin/', admin.site.urls),
]

```



대신

```http://127.0.0.1:8000/dinner/```  그 전엔 주소를 이렇게 쳤는데

```http://127.0.0.1:8000/pages/dinner/``` 이제는 이렇게 쳐야됨





그리고 새로 만든 앱의 url에서도

```
from django.urls import path
from . import views

urlpatterns = [
    
]
```

이렇게 골격을 만듬







근데 기존 앱인 pages에도 index 함수가 있고 새로만든 utilities에도 index 가 있으면

setting에 적혀있는 순서대로 찾아서 가장 위에 있는 utilities에 있는 index만 불러온다.



그래서 구별해주기 위해 templates 폴더 안에 app 이름과 동일한 폴더명을 가진 폴더를 만들어 html 파일들을 거기에 넣어줌.

그리고 views에서  return할때 앞에 폴더명을 붙여줘야함

이렇게.

```python
def index(request):
    return render(request, 'pages/index.html')
```

```python
def index(request):
    return render(request, 'utilities/index.html')
```







## 상속

1. 프로젝트 안에 폴더를 생성하고 안에 상속할 html 파일을 만들어줌

2. setting의 TEMPLATES 리스트에 DIR에서 상속할 html의 경로를 지정해줌.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



3. 상속받을 html 파일에서 상속받는다는 표시를 해줌

```html
{% extends 'base.html' %}

{% block body %}
기존 html 내용
{% endblock %}
```

이렇게

