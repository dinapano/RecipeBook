"""
URL configuration for recipebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', views.RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', views.RecipeRetrieveUpdateDestroyView.as_view(), name='recipe-detail'),
]

#code explanation:
'''1.We import the necessary modules from Django and our views from the 'recipes' app. 
   2.We define the urlpatterns list which contains the URL patterns for our API views. 
   3.The path('recipes/') pattern maps to the RecipeListCreateView, allowing users to list all recipes or add a new recipe. 
   4.The path('recipes/<int:pk>/') pattern maps to the RecipeRetrieveUpdateDestroyView, allowing users to retrieve, update, or 
     delete a specific recipe based on its primary key (pk).'''