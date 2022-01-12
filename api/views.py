from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Tag, ServingSize, Ingredient, Recepie, RecepieLine
from .serializers import TagSerializer, ServingSizeSerializer, IngredientSerializer, RecepieSerializer, RecepieLineSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)


class ServingSizeViewSet(viewsets.ModelViewSet):
    queryset = ServingSize.objects.all()
    serializer_class = ServingSizeSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # IsAuthenticated prilokom get potrebna autentifikacija

    # @action(detail=True, methods=['PATCH'])
    @action(detail=True, methods=['POST'])
    def update_kcl(self, request, pk=None):
        #pk is primary key
        if 'kcal' in request.data:
            kcal = request.data.get('kcal')
            user = request.user

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

    #override metode iz ModelViewSet
    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update kcl like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create ingredient like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RecepieViewSet(viewsets.ModelViewSet):
    queryset = Recepie.objects.all()
    serializer_class = RecepieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    #AllowAny prilokom get nije potrebna autentifikacija

class RecepieLineViewSet(viewsets.ModelViewSet):
    queryset = RecepieLine.objects.all()
    serializer_class = RecepieLineSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )




