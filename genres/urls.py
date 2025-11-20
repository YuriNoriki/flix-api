from django.urls import path
from . import views

urlpatterns = [

    path('genres/', views.GenresCreateListView.as_view(), name ='genre_list_view'),
    path('genres/<int:pk>/',views.GenresRetrieveUpdateDestroyView.as_view() ,name ='genre_detail_view'),

]