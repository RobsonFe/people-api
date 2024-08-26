from uuid import uuid4
import uuid
from django.db import models


class People(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255, default="João Silva")
    email = models.EmailField(unique=True, default="user.email@email.com")
    idade = models.IntegerField(default=30)
    profissao = models.CharField(max_length=255, default="Desenvolvedor")
    salario = models.DecimalField(
        max_digits=10, decimal_places=2, default=5.000)


class Meta:
    verbose_name = 'People'
    verbose_name_plural = 'Peoples'
    indexes = [
        models.Index(fields=['nome']),  # pegar index pelo nome
    ]


def __str__(self):
    return self.nome
