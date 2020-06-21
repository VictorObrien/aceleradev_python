from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.


def validate_level(level_value):
    if level_value not in ["CRITICAL", "DEBUG", "ERROR", "WARNING", "INFO"]:
        raise ValidationError(
            f"{level_value} not a valid level.", params={"level_value": level_value}
        )


class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Último acesso', auto_now=True)
    email = models.EmailField('Email')
    password = models.CharField('Senha', max_length=50, validators=[
                                MinLengthValidator(8)])

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Ambiente', max_length=20)
    version = models.CharField('Versão', max_length=5)
    address = models.GenericIPAddressField('Endereço IPV4', max_length=39)

    def __str__(self):
        return self.name


class Event(models.Model):
    LEVELS = [(level, level)
              for level in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']]

    level = models.CharField('Nível', max_length=20,
                             choices=LEVELS, validators=[validate_level])
    data = models.TextField('Dados')
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Data', auto_now=True)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.level


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.group.name} - {self.user.name}'
