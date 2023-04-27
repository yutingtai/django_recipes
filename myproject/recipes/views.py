import dataclasses
import random
from typing import List
from django.http import HttpRequest, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render
from .models import RecipeDbModel, StepsDbModel, IngredientsDbModel
from django.urls import reverse


# Create your views here.

@dataclasses.dataclass
class RecipeCard:
    title: str
    description: str
    id_number: int


@dataclasses.dataclass
class HomePageUi:
    recipes: List[RecipeCard]


def home_page(request):
    recipe_model_list: List[RecipeDbModel] = [recipe_model for recipe_model in RecipeDbModel.objects.all()]
    recipe_random_model_list: List[RecipeDbModel] = random.sample(recipe_model_list, 3)
    recipe_list = []
    for recipe_model in recipe_random_model_list:
        recipe_list.append(
            RecipeCard(
                title=recipe_model.name_of_recipe,
                description=recipe_model.stepsdbmodel_set.all()[0],
                id_number=recipe_model.pk
            )
        )
    ui_state = HomePageUi(
        recipes=recipe_list
    )

    context = {
        "state": ui_state
    }
    return render(request, 'recipes/index_page.html', context)


@dataclasses.dataclass
class RecipeDetailUi:
    title: str
    author_name: str
    steps: str
    ingredients: str
    clap_count: int


def recipe_detail(request, recipe_id: int):
    recipe: RecipeDbModel = RecipeDbModel.objects.get(pk=recipe_id)
    recipe_steps = [step.description for step in recipe.stepsdbmodel_set.all()]
    recipe_ingredients = [ingredient.content_of_ingredient for ingredient in recipe.ingredientsdbmodel_set.all()]
    ui_state = RecipeDetailUi(
        title=recipe.name_of_recipe,
        author_name=recipe.name_of_author,
        steps=recipe_steps,
        ingredients=recipe_ingredients,
        clap_count=recipe.claps
    )

    context = {
        "state": ui_state
    }
    return render(request, 'recipes/recipe_detail.html', context)


def new_recipe_form(request):
    return render(request, 'recipes/new_recipe_page.html')


def create_new_recipe(request: HttpRequest):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    title: str = request.POST['title']
    author_name: str = request.POST['author_name']
    steps: List[str] = request.POST['steps']
    ingredients: List[str] = request.POST['ingredients']

    new_recipe = RecipeDbModel(
        name_of_recipe=title,
        name_of_author=author_name,
        claps=0,
    )
    new_recipe.save()


    step_db_object = StepsDbModel(
        description=steps,
        recipe=new_recipe,
    )
    step_db_object.save()

    ingredient_db_object = IngredientsDbModel(
        content_of_ingredient=ingredients,
        recipe=new_recipe,
    )
    ingredient_db_object.save()

    return HttpResponseRedirect(
        redirect_to=reverse(
            viewname="recipes:recipe_detail_page",
            args=(new_recipe.pk,)
        )
    )
