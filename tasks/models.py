from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  club2 = models.TextField(max_length=200)
  fecha = models.TextField(max_length=201,null=True)  
  golesclub = models.TextField(max_length=200,default=0,blank=True, null=True)
  golesclub2 = models.TextField(max_length=200,default=0,blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title + ' - ' + self.user.username
