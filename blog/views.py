from django.shortcuts import render
# Create your views here.

posts=[
    {
        'author':'John Doe',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 27, 2012'
    },
    {
        'author':'Titania Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'July 05, 2022'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html',title='about')