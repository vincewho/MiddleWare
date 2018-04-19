from django.db import models
from django.utils import timezone

# Create your models here.


class comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    message_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        pass
