from django.db import models
from apps.perfil.models import PerfilUser

# Create your models here.
class Atendente(models.Model):
    user = models.ForeignKey(PerfilUser, on_delete=models.CASCADE)

    