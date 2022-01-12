from rest_framework import serializers
from .models import Tag, ServingSize, Ingredient, Recepie, RecepieLine
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # onemogučimo da vrati password
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user


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

