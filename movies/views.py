from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer

class MoviewCreateListView(generics.ListCreateAPIView):
    queryset = Movie
    serializer_class = MovieSerializer

class MovieRetrieverUpdateDestroy(generics.RetrieveDestroyAPIView):
    queryset = Movie
    serializer_class = MovieSerializer