from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

# All post with function view
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context=context)

# All post with list view
class PostListView(ListView):
    model=Post
    template_name='blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']

# Single post with detail view
class PostDetailView(DetailView):
    model=Post

def about(request):
    context={
        'title':'About'
    }
    return render(request,'blog/about.html',context=context)