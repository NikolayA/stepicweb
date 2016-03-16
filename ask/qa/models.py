from django.db import models
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User,db_constraint=False, default=1)
  likes = models.ManyToManyField(User, related_name='likes_')
  def __str__(self):
        return self.title
  def get_url(self):
        return 'http://0.0.0.0/question/' + str(self.id) + '/' 

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User, db_constraint=False)
  def __str__(self):
        return self.text

class User(models.Model):
    login = models.CharField(unique=True)
    password = models.CharField()
    email = models.EmailField()

class Session(models.Model):
    key = models.CharField(unique=True)
    user = models.ForeignKey(User)
    expires = models.DateTimeField()

