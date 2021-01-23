from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    pages = models.PositiveIntegerField()
    price = models.FloatField()
    def get_absolute_url(self):
        return reverse('Book-detail', kwargs={'pk': self.pk})
