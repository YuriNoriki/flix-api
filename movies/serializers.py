from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    # campos de validação
    def validate_realese_data(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo não pode ser mais de 500 caracteres')
        return value
    
    # campo calculado 
    def get_rate(self, obj):

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate
        
        return None
        
        # reviews é o nome da ligação no model de reviews 
        #reviews = obj.reviews.all()
        
        #if reviews:
            #sum_reviews = 0

            # É AQUI que o QuerySet é avaliado e os dados SÃO carregados:
            #for review in reviews:
                # É AQUI que o campo 'stars' de cada objeto 'review' é acessado:
                #sum_reviews += review.stars

            #reviews_count = reviews.count()

            #return round(sum_reviews / reviews_count, 1)
        
        #return None