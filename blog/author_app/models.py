from django.db import models


class Author(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    year_of_birth = models.SmallIntegerField()
    country = models.CharField(max_length= 255)
    biography = models.TextField()
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    
    

