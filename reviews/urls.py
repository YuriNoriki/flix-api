from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewCreateListViews.as_view(), name = 'reviews_list_view'),
    path('reviews/<int:pk>/', views.ReviewRetrieverUpdateDestroy.as_view(), name = 'reviews_detail_view'),

]
