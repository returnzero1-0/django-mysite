from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'dhaval',
        'title':'Blog post 1',
        'content':'First post content',
        'data_posted':'Nov-13,2020'
    },
    {
        'author':'gaurav',
        'title':'Blog post 2',
        'content':'Second post content',
        'data_posted':'Nov-23,2020'
    },
]

def home(request):
    context={
        'posts':posts,
        'title':' - Home'
    }
    return render(request,'blog/home.html',context)
    

def about(request):
    context={
        'title':' - About'
    }
    return render(request,'blog/about.html',context)