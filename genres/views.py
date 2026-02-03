from django.http import JsonResponse
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from genres.permission import GenresPermissionClass

class GenresCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenresPermissionClass)

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 

