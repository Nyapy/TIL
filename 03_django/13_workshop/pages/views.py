from django.shortcuts import render

# Create your views here.

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