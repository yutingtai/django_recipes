from django.db import models


# Create your models here.
class RecipeDbModel(models.Model):
    name_of_recipe = models.CharField(max_length=100)
    name_of_author = models.CharField(max_length=50)
    claps = models.IntegerField()

    def __str__(self):
        return self.name_of_recipe


class IngredientsDbModel(models.Model):
    content_of_ingredient = models.CharField(max_length=200)
    recipe = models.ForeignKey(RecipeDbModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.content_of_ingredient


class StepsDbModel(models.Model):
    description = models.CharField(max_length=300)
    recipe = models.ForeignKey(RecipeDbModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
