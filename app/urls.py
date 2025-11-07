from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenresCreateListView, GenresRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieverUpdateDestroyView
from movies.views import MoviewCreateListView, MovieRetrieverUpdateDestroy 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenresCreateListView.as_view(), name ='genre_list_view'),
    path('genres/<int:pk>/',GenresRetrieveUpdateDestroyView.as_view() ,name ='genre_detail_view'),

    path('actors/',ActorCreateListView.as_view(), name ='actor_create_list'),
    path('actors/<int:pk>/',ActorRetrieverUpdateDestroyView.as_view() ,name ='genre_detail_view'),

    path('movies/', MoviewCreateListView.as_view(), name = 'movies_list_view'),
    path('movies/<int:pk>/', MovieRetrieverUpdateDestroy.as_view(), name = 'movies_detail_view'),

]
