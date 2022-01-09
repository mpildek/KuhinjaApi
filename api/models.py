from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ServingSize(models.Model):

    qty = models.IntegerField()
    uom = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.qty} {self.uom}'



class Ingredient(models.Model):

    name = models.CharField(max_length=32, unique=True)
    image = models.ImageField(blank=True)
    description = models.TextField(max_length=360)
    serving = models.ForeignKey(ServingSize,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="serving")
    kcal = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recepie(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(blank=True)
    description = models.TextField(max_length=360)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def no_of_ingredients(self):
        ingredient_ids = []
        recepie_lines = RecepieLine.objects.filter(recepie=self)
        for recepie_line in recepie_lines:
            ingredient_ids.append(recepie_line.ingridient_id)
        ingredients = Ingredient.objects.filter(id__in=ingredient_ids)
        return len(ingredients)

    def no_of_kcal(self):
        recepie_lines = RecepieLine.objects.filter(recepie=self)
        kcal = sum([recepie_line.ingridient.kcal * recepie_line.no_of_servings for recepie_line in recepie_lines])
        return kcal


class RecepieLine(models.Model):
    no_of_servings = models.FloatField()
    ingridient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recepie = models.ForeignKey(Recepie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.no_of_servings} {self.ingridient}'













