RECIPE BOOK:
------------
These are the steps that were followed throughout this project:

Backend Setup:
--------------
1.Initialize a new Django project and create a new app, say recipes.

2.In the models.py of the recipes app, define a Recipe model with fields: recipe_name, ingredients (as a text field where ingredients are listed line by line), and instructions.

3.Use Django migrations to create the database schema.

4.Set up Django Rest Framework and create a serializer for the Recipe model.

5.In views.py, create API views for listing all recipes, adding a new recipe and deleting a recipe.

6.Configure the URLs for the API endpoints.

Frontend Setup:
---------------
1.Initialize a new React app using Create React App.

2.Install necessary packages like Axios for API calls.

3.Create a RecipeList component to fetch and display all recipes from the Django API.

4.Create an AddRecipe component with a form to submit a new recipe. On submission, make a POST request to the Django API.

5.In the RecipeList component, add a delete button next to each recipe. On click, make a DELETE request to the Django API.

6.Style the components using CSS or a library like Bootstrap for a clean look.

Database Configuration:
-----------------------
1.Stick with Django's default SQLite database. This requires no additional setup.

2.Ensure the Recipe model is migrated to create the corresponding database table.

Testing and Final Touches:
--------------------------
1.Test the Django API endpoints using a tool like Postman to ensure they work as expected.

2.In the React app, ensure that the list of recipes updates in real-time when a new recipe is added or an existing one is deleted.

3.Add basic error handling in the React app, e.g., display an error message if the API call fails.
