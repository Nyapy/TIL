from django.urls import path
from . import views

urlpatterns = [
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