from os import name
from tabnanny import verbose

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
# Create your models here.
class Users(AbstractUser):
    balance= models.DecimalField(decimal_places=2, max_digits=11, null=False, verbose_name="Баланс", default=0)

    def __str__(self):
        return f"{self.username}-{self.balance}"

class Operation(models.Model):
    class Type(models.TextChoices):
        DEPOSIT = "deposit", "пополнение"
        WITHDRAW = "withdraw", "снятие"
        TRANSFER = "transfer", "перевод"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Получатель", null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=11, verbose_name="Сумма", null=False)
    operation_type = models.CharField(max_length=12, choices=Type.choices, verbose_name="Тип операции")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дейта")