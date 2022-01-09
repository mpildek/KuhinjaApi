from django.contrib import admin
from .models import Tag, ServingSize, Ingredient, Recepie, RecepieLine

admin.site.register(Tag)
admin.site.register(ServingSize)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'serving', 'kcal']
    list_filter = ['tags', 'vegan']
    search_fields = ['name']


@admin.register(RecepieLine)
class RecepieLineAdmin(admin.ModelAdmin):
    list_display = ['no_of_servings', 'ingridient']


class RecepieLineInLine(admin.TabularInline):
    model = RecepieLine

@admin.register(Recepie)
class RecepieAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [RecepieLineInLine]
