from django.db import models
from datetime import datetime
class Info(models.Model):
    name    = models.CharField(max_length=25)
    image   = models.ImageField(upload_to='dog_images', blank=False)
    date    = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
        