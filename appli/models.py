from django.db import models

# Create your models here.


class Articles(models.Model):

    name = models.CharField("Nom de l'article", max_length=255)
    article = models.TextField("Ecrire l'article", blank=True, null=True)

    def __str__(self):
        return self.name
