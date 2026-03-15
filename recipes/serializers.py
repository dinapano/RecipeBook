#A serializer converts complex data (like database models) into formats that can be sent over an API, usually JSON, 
#and can also convert JSON back into Python objects.
from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'recipe_name', 'ingredients', 'instructions']

#code explanation:
'''1.We import the necessary modules from Django Rest Framework and our Recipe model. 
   2.We define the RecipeSerializer class which inherits from serializers.ModelSerializer. 
   3.In the Meta class, we specify the model (Recipe) and the fields we want to serialize (id, recipe_name, ingredients, and instructions). '''