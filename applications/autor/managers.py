from django.db import models


class AutorManager(models.Manager):
    """Managers para el modelo autor"""

    def listarAutores(self):
       return self.all()
