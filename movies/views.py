from rest_framework import generics, views, response, status
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission
from django.db.models import Count, Avg
from reviews.models import Review

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieverUpdateDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Define a classe de visualização para estatísticas de filmes usando a base do Django Rest Framework
class MovieStatsView(views.APIView):
    #Define as classes de permissão: usuário autenticado e permissões globais do sistema
     permission_classes = (IsAuthenticated,GlobalDefaultPermission)
     # Define o conjunto de dados base (todos os filmes) para as consultas
     queryset = Movie.objects.all()

    # Define o método que lidará com as requisições do tipo GET
     def get(self, request):
        # Conta a quantidade total de filmes registrados no banco de dados
         total_movies = self.queryset.count()
         # Agrupa filmes por nome de gênero e conta quantos filmes existem em cada um
         movies_by_genre = self.queryset.values('genre__name').annotate(count = Count('id'))
         # Conta o total de avaliações registradas na tabela Review
         total_reviews = Review.objects.count()
         # Calcula a média aritmética de todas as notas (estrelas) dadas nas avaliações
         average_stars = Review.objects.aggregate(avg_stars = Avg('stars'))['avg_stars']
         
         # Retorna uma resposta JSON com os dados processados e o status HTTP 200 (OK)
         return response.Response(data={
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
         }, status=status.HTTP_200_OK)