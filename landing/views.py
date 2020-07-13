from django.shortcuts import render
from .models import Mylessons,Blog
from django.views.generic import ListView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import BlogForm
class MyLessonsView(ListView):
    model = Mylessons
    template_name = 'landing/index.html'
    paginate_by = 2
class MyLessonsDetailView(DetailView):
    model = Mylessons
    template_name = 'landing/DetailView.html'
    context_object_name = 'elem'
class BlogView(SuccessMessageMixin, CreateView,ListView):
    model = Blog
    template_name = 'landing/blog.html'
    form_class = BlogForm
    success_url = '/'
    success_message = "Ваше сообщение отправлено!"
class BlogUpdate(SuccessMessageMixin, UpdateView):
    model = Blog
    fields = ['text']
    template_name = 'landing/blog_update.html'
    success_url = '/blog'
    success_message = "Запись сохранена!"
class BlogDelete(SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'landing/blog_delete.html'
    success_url = '/blog'
    success_message = "Запись удалена!"

# Create your views here.
