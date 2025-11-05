from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenresCreateListView,GenresRetrieveUpdateDestroyView
from actors.views import ActorCreateListView,ActorRetrieverUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenresCreateListView.as_view(), name ='GenresCreateListView'),
    path('genres/<int:pk>/',GenresRetrieveUpdateDestroyView.as_view() ,name ='genre_detail_view'),

    path('actors/',ActorCreateListView.as_view(), name ='actor_create_list'),
    path('actors/<int:pk>/',ActorRetrieverUpdateDestroyView.as_view() ,name ='genre_detail_view'),

]
