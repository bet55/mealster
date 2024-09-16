from django.db import models


class Ingredient(models.Model):
    api_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Recipie(models.Model):
    api_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE) #we guarantee to never delete ingredients from db
    measures = models.JSONField(default=list)
    instructions = models.TextField(blank=True)
    picture = models.ImageField(upload_to="recipes/", blank=True)
    youtube_link = models.URLField(blank=True)
