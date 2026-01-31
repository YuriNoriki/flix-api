from django.shortcuts import render
from reviews.models import Review
from rest_framework import generics
from reviews.serializers import ReviewSerializers
from rest_framework.permissions import IsAuthenticated

class ReviewCreateListViews(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class ReviewRetrieverUpdateDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
