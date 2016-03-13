from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
  title = models.CharField()
  text = models.TextField()
  added_at = models.DateTimeField()
  rating = models.IntegerField()
  author = models.ForeignKey(User)
  likes = models.ManyToManyField(User, related_name='likes_') 

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField()
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)
