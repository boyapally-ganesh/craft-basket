from django.shortcuts import render
from post .models import* 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . forms import postform, editform
from django.urls import reverse_lazy
# Create your views here.

class homepage(ListView):
    model = post
    template_name = 'post/home.html'
    cats = Category.objects.all
    ordering = ["-post_time"]


    """def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(homepage, self.get_context_data(*args, **kwargs))
        context["cat_menu"] = cat_menu
        return context"""
class detail(DetailView):
    model = post
    template_name = 'post/detail.html'

"""
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(detail, self.get_context_data(*args, **kwargs))
        context["cat_menu"] = cat_menu
        return context"""

def showdata(request, category):
    cat = post.objects.get(category=category)
    return render(request, 'post/home.html',{'cat':cat})
    print(cat)
class createpost(CreateView):
    model = post
    form_class = postform
    template_name = "post/addpost.html"
    #fields = ()

class updatepost(UpdateView):
    model = post
    form_class = editform
    template_name = 'post/update.html'
    #fields=['title','body']
class deletepost(DeleteView):
    model = post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('home')

def categoryview(request, cats):
    category_posts = post.objects.filter(category=cats)
    return render(request, 'post/categories.html', {'cats':cats, "category_posts":category_posts})
