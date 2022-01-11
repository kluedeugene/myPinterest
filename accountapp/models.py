from django.db import models

# Create your models here.


class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)  # null = 필요한지 안한지. false= 필요
