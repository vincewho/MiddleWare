from django.db import models

# Create your models here.


class NameModel(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()


class ContactModel(models.Model):
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=20)
    sender = models.EmailField()
    cc_myself = models.BooleanField()


class team(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name
