from django.db import models

class Dish(models.Model):
    dish_name=models.CharField(max_length=50)
    cook_name=models.CharField(max_length=50)

    def __str__(self):
        return self.dish_name


class Recipie(models.Model):
    dish_name=models.ForeignKey("Dish", on_delete=models.CASCADE, related_name='Recipie')
    ingredients=models.TextField()
    Recipie=models.TextField() 

