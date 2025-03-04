from django.db import models

class LPProblem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.