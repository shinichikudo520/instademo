# from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView

from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy

from Insta.models import Post

# Create your views here.

class HelloDjango(TemplateView):
    template_name = 'home.html'
    
class PostView(ListView):
    model  = Post
    template_name = 'posts.html'

class PostDetail(DetailView):
    model  = Post
    template_name = 'post_detail.html'

# 创建表单
class PostCreateView(CreateView):
    model  = Post
    template_name = 'make_post.html'
    fields =  '__all__' # 指定用户需要输入的Post类中的哪些属性

# 更新表单
class PostUpdateView(UpdateView):
    model  = Post
    template_name = 'update_post.html'
    fields =  ('title',) # 指定用户需要输入的Post类中的哪些属性，如果不是所有属性，则传一个元组 'title'后的一个，也是必须的

# 删除表单
class PostDeleteView(DeleteView):
    model  = Post
    template_name = 'delete_post.html'
    # 删除成功  重定向路径，reverse_lazy与reverse的区别  就是删除请求与重定向的跳转是同时进行的
    success_url = reverse_lazy('home')
