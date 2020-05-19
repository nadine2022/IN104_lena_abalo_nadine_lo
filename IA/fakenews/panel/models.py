from django.db import models

# Create your models here.
class Article(models.Model):

    source=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    pub_date=models.DateTimeField('date published')

        
    def __str__(self):
        return self.source
