from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import ListView,DetailView 
from django.views.generic.edit import UpdateView,DeleteView,CreateView

from django.urls import reverse_lazy 


from .models import Article 

# Create your views here.

class ArticleListView(ListView):
    model = Article 
    template_name = 'articles/article_list.html'

class ArticleDetailsView(DetailView):
    model = Article 
    template_name = 'articles/article_details.html'

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article 
    fields = ('title','body') 
    template_name = 'articles/article_edit.html'
    login_url = 'login'


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article 
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article 
    template_name = 'articles/article_new.html'
    fields = ('title','body')
    login_url = 'login'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
