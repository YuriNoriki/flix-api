from django.http import JsonResponse
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer

class GenresCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 

