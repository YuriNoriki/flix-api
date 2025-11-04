from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenresCreateListView,genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenresCreateListView.as_view(), name ='GenresCreateListView'),
    path('genres/<int:pk>/',genre_detail_view, name ='genre_detail_view'),
]
