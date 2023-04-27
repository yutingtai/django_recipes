from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('recipe_detail/<int:recipe_id>/', views.recipe_detail, name="recipe_detail_page"),
    path('new_recipe_form/', views.new_recipe_form, name='new_recipe_form'),
    path('create_new_recipe/', views.create_new_recipe, name='create_new_recipe'),
]
