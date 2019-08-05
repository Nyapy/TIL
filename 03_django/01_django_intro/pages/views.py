from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def image(request):
    return render(request, 'image.html')

#2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ('족발', '햄버거', '피자', '초밥')
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

#3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '피자', '초밥']
    pick = random.choice(menu)
    context = {'name':name,
        'age': age,
        'pick': pick}
    return render(request, 'hello.html', context)


#4. 실습
#4-1. 동적 라우팅을 활용해서 (name과 age를 인자로 받아) 자기소개 페이지
#4-2. 두 개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력

def I(request, name, age):
    context = {'name':name, 'age': age}
    return render(request, 'I.html', context)

def mul(request, num1, num2):
    context = {'num1': num1, 'num2': num2, 'num3' : num2*num1 }
    return render(request, 'mul.html', context)

#4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.

def area(request, r):
    pi = 3.14
    context = {'r': r, 'area': pi*r**2 }
    return render(request, 'area.html', context )

#4. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is shor, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetimenow = datetime.now

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,

    }
    return render(request, 'template_language.html', context)

def info(request):
    return render(request, 'class.html')

def student(request, name):

    dictionary = {'박길동': 28,
    '남수경': 56,
    '이현우': 19,}
    
    context = {
        'name': name,
        'age': dictionary.get(name) 
    } 
    return render(request, 'student.html', context)