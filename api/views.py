from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Rating, Meal
from .serializers import RatingSerializer, MealSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class  = MealSerializer

    @action(methods=['POST'], detail=True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            Create or update
            '''
            meal = Meal.objects.get(pk=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)
            try:
                #UPDATE
                rating = Rating.objects.get(user=user.id, meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Stars updated successfully',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)
            except:
                #CREATE
                rating = Rating.objects.create(stars=stars, user=user, meal=meal)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Stars added successfully',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)

        else:
            json={
                'message':'There is no stars provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
