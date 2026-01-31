from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'ESTADOS UNIDOS'),
    ('BR', 'BRASIL'),
    

)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    nationality = models.CharField(
        max_length = 200,
        choices = NATIONALITY_CHOICES,
        blank= True,
        null=True,
    )

    def __str__(self):
        return self.name
