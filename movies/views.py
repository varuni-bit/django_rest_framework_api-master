from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

#views for different gener of movies
class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer

class SciFiViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='sci-fi')
    serializer_class = MovieSerializer

class HorrorViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='horror')
    serializer_class = MovieSerializer

class CartoonViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='animation')
    serializer_class = MovieSerializer