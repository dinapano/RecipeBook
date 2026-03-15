from django.shortcuts import render
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

#code explanation:
'''1. We import the necessary modules from Django Rest Framework, our Recipe model, and the RecipeSerializer.
   2.We define the RecipeListCreateView class which inherits from generics.ListCreateAPIView. 
     This view will handle listing all recipes and adding a new recipe. 
   3.We define the RecipeRetrieveUpdateDestroyView class which inherits from generics.RetrieveUpdateDestroyAPIView. 
     This view will handle retrieving a specific recipe, updating a recipe, and deleting a recipe. '''