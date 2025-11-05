from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenresCreateListView,GenresRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenresCreateListView.as_view(), name ='GenresCreateListView'),
    path('genres/<int:pk>/',GenresRetrieveUpdateDestroyView.as_view() ,name ='genre_detail_view'),
]
