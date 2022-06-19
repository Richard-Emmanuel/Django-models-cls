from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
  Title = models.CharField(max_length=200)
  Text  = models.TextField()
  Author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  Created_date = models.DateTimeField()
  Published_date = models.DateTimeField()

  class Meta:
        db_table = ''
        managed = True
        verbose_name_plural = 'Posts'

  def __str__(self) -> str:
        return (f"{self.Title} by {self.Author}").__str__()

 