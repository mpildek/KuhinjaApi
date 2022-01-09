from rest_framework import serializers
from .models import Tag, ServingSize, Ingredient, Recepie, RecepieLine


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class ServingSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServingSize
        fields = ('id', 'qty', 'uom')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'tags', 'vegan', 'serving', 'kcal')

        def to_representation(self, instance):
            self.fields['serving'] = ServingSizeSerializer(read_only=True)
            self.fields['tags'] = TagSerializer(read_only=True)
            return super(IngredientSerializer, self).to_representation(instance)


class RecepieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepie
        fields = ('id', 'name', 'description', 'tag', 'no_of_ingredients', 'no_of_kcal')
        #no_of_ingredients, no_of_kcal is method from models


class RecepieLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepieLine
        fields = ('id', 'no_of_servings', 'ingridient', 'recepie')

