from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name = 'movies_list_view'),
    path('movies/<int:pk>/', views.MovieRetrieverUpdateDestroy.as_view(), name = 'movies_detail_view'),
]
