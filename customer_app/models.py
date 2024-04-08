from django.db import models
from django.urls import reverse

# Create your models here.
class PreWorkout(models.Model):

    RATING_CHOICES = [
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]

    name = models.CharField(max_length=100)
    nonStim = models.BooleanField(default=False)
    totalServings = models.PositiveIntegerField()
    sizeInOz = models.FloatField()
    reviewOutOfFive = models.PositiveIntegerField(choices=RATING_CHOICES, default=3)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('preworkout-detail', args=[str(self.id)])

"""
class Ingredient(models.Model):

    pre_workout = models.ForeignKey(PreWorkout, related_name='ingredients', on_delete=models.CASCADE)

    INGREDIENTS = (('Caffeine', 'Caffeine'), ('Beta-Alanine', 'Beta-Alanine'), ('Creatine', 'Creatine'), ('Citrulline Malate', 'Citrulline Malate'), 
                   ('L-Arginine', 'L-Arginine'), ('Nitrate', 'Nitrate'), ('Taurine', 'Taurine'), ('L-Tyrosine', 'L-Tyrosine'), 
                   ('Betaine Anhyndrous', 'Betaine Anhyndrous'), ('L-Theanine', 'L-Theanine'), ('L-Carnitine', 'L-Carnitine'), 
                   ('Glutamine', 'Glutamine'), ('Vitamin D', 'Vitamin D'), ('Coenzyme Q10 (CoQ10)', 'Coenzyme Q10 (CoQ10)'), 
                   ('Rhodiola Rosea', 'Rhodiola Rosea'), ('Yerba Mate', 'Yerba Mate'), ('Green Tea Extract', 'Green Tea Extract'), 
                   ('AlphaSize', 'AlphaSize'), ('HICA', 'HICA'), ('Theobromine', 'Theobromine'), ('AstraGin', 'AstraGin'), 
                   ('Huperzia Serrata', 'Huperzia Serrata'))

    ingredientName = models.CharField(max_length=200, choices=INGREDIENTS)
    dosage = models.PositiveIntegerField()

    def __str__(self):
        return self.pre_workout
    
    def get_absolute_url(self):
        return reverse('ingredient-detail', args=[str(self.id)])
"""