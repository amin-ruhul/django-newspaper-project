from django.shortcuts import render
from django.views.generic import ListView,DetailView 
from django.views.generic.edit import UpdateView,DeleteView 

from django.urls import reverse_lazy 


from .models import Article 

# Create your views here.

class ArticleListView(ListView):
    model = Article 
    template_name = 'articles/article_list.html'

class ArticleDetailsView(DetailView):
    model = Article 
    template_name = 'articles/article_details.html'

class ArticleUpdateView(UpdateView):
    model = Article 
    fields = ('title','body') 
    template_name = 'articles/article_edit.html'


class ArticleDeleteView(DeleteView):
    model = Article 
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')