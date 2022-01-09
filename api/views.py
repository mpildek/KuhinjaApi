from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Tag, ServingSize, Ingredient, Recepie, RecepieLine
from .serializers import TagSerializer, ServingSizeSerializer, IngredientSerializer, RecepieSerializer, RecepieLineSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ServingSizeViewSet(viewsets.ModelViewSet):
    queryset = ServingSize.objects.all()
    serializer_class = ServingSizeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    # @action(detail=True, methods=['PATCH'])
    @action(detail=True, methods=['POST'])
    def update_kcl(self, request, pk=None):
        #pk is primary key
        if 'kcal' in request.data:
            kcal = request.data.get('kcal')
            # user = request.user
            user = User.objects.get(id=1)
            try:
                ingredient = Ingredient.objects.get(id=pk)
                ingredient.kcal = kcal
                ingredient.save()
                serializer = IngredientSerializer(ingredient, many=False)
                response = {'message': 'Kcl updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                response = {'message': 'You need to provide PK'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {'message': 'You need to provide kcl'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class RecepieViewSet(viewsets.ModelViewSet):
    queryset = Recepie.objects.all()
    serializer_class = RecepieSerializer


class RecepieLineViewSet(viewsets.ModelViewSet):
    queryset = RecepieLine.objects.all()
    serializer_class = RecepieLineSerializer




