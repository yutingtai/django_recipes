from django.contrib import admin

# Register your models here.
from .models import RecipeDbModel, IngredientsDbModel, StepsDbModel

admin.site.register(RecipeDbModel)
admin.site.register(IngredientsDbModel)
admin.site.register(StepsDbModel)
