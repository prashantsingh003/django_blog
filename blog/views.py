from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( 
    UpdateView, 
    CreateView, 
    ListView, 
    DetailView,
    DeleteView
    )
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


class PostCreateView(LoginRequiredMixin, CreateView):  # <app>/<model>_form.html
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PosUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # <app>/<model>_form.html
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False


def about(request):
    context={
        'title':'About'
    }
    return render(request,'blog/about.html',context=context)