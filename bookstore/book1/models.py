from django.db import models
from django.db.models.deletion import CASCADE


class Book(models.Model):
    name = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    pubDate = models.DateField()
    price = models.IntegerField()

# Create your models here.
class Review(models.Model):
    article = models.ForeignKey(Book,on_delete=CASCADE)
    content = models.IntegerField()
    
    def __str__(self):
        return self.article.title + '-' + str(self.id)