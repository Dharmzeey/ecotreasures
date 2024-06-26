from django.db import models

class ExhibitionPlace(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()
  image = models.ImageField(upload_to="exhibitions")
  location = models.CharField(max_length=200)
  def __str__(self):
    return self.name
