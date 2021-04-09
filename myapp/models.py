from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    jmbg = models.CharField(max_length=13)