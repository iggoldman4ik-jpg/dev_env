from os import name
from tabnanny import verbose

from django.db import models

# Create your models here.
class Users(models.Model):
    name= models.CharField(max_length=35, unique=True, verbose_name="Имя")
    balance= models.DecimalField(decimal_places=2, max_digits=11, verbose_name="Баланс")

    def __str__(self):
        return f"{self.name}-{self.balance}"

    class Meta:
        db_table="users"
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"
        
        