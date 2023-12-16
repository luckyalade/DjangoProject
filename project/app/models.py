from django.db import models

# Create your models here.


class SignUp(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.firstName
