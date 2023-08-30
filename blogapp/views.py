from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Joe Tim',
        'title': 'Blog 1',
        'content': 'First post content',
        'datePosted': 'August 27, 2023'
    },
    
    {
        'author': 'Ray Brian',
        'title': 'Blog 2',
        'content': 'Second post content',
        'datePosted': 'August 30, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)


def about(request):
    return render(request, 'blogapp/about.html', {'title':'about'})