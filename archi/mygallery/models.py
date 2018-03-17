from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=40, unique=True)
    image = models.ImageField(upload_to='mygallery/img')
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
