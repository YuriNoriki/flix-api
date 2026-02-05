from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieverUpdateDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer