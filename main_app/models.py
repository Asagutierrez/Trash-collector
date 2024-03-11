from django.db import models
from django.urls import reverse

# Create your models here.
class Trash(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  piecesOfTrash = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('trash-detail', kwargs={'trash_id': self.id})