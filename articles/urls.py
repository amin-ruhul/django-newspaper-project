from django.urls import path 

from .views import ArticleListView,ArticleUpdateView,ArticleDetailsView,ArticleDeleteView

urlpatterns = [
    path('',ArticleListView.as_view(),name = 'article_list'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name = 'article_edit'),
    path('<int:pk>/',ArticleDetailsView.as_view(),name = 'article_details'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name = 'article_delete'),
    
]