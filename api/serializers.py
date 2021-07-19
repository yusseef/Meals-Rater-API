from rest_framework import serializers
from .models import Rating, Meal

class MealSerializer(serializers.modelserializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'stars', 'meal')