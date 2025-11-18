from django.shortcuts import render
from reviews.models import Review
from rest_framework import generics
from reviews.serializers import ReviewSerializers

class ReviewCreateListViews(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class ReviewRetrieverUpdateDestroy(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
