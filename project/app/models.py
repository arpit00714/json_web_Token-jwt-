from django.db import models
  
class MovieModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    def __str__(self):
        return self.title

class StudentModel(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name