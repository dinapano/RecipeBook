from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.recipe_name

#code explanation:
'''1.We import the necessary modules from Django. 
   2.We define the Recipe class which inherits from models.Model. 
   3.The recipe_name field is a character field with a maximum length of 255 characters. 
   4.The ingredients and instructions fields are text fields, allowing for longer text entries. 
   5.The __str__ method returns the recipe name, which will be useful for display purposes in the Django admin 
     interface or any other place where a string representation of the model is needed. '''