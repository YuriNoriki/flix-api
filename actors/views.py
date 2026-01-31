from django.shortcuts import render
from actors.models import Actor
from rest_framework import generics
from actors.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieverUpdateDestroyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
