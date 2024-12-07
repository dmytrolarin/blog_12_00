from django.db import models
from author_app.models import Author
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null = True)

    def get_absolute_url(self):
        return reverse('view_post', kwargs = {'pk': self.pk})
