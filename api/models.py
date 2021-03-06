from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal = self)
        return(len(ratings))

    def avg_rating(self):
        #sum of ratings / len
        sum = 0
        ratings = Rating.objects.filter(meal=self) #number of ratings of the meal
        for x in ratings:
            sum += x.stars
        if len(ratings) > 0:
            return sum / len(ratings)

        else:
            return 0

    def __str__(self):
        return self.title

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)


