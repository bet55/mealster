from django.contrib.auth.models import User
from django.db import models

from mealster.recipies.models import Recipie, Ingredient


class AppUser(User):
    favorite_recipie = models.ForeignKey(Recipie, default=None, on_delete=models.CASCADE)
    banned_ingredient = models.ForeignKey(Ingredient, default=None, on_delete=models.CASCADE) #we guarantee to never delete ingredients from db
