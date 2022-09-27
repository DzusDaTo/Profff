from django.db import models


class Device(models.Model):
    Name = models.CharField(max_length=100, verbose_name='Имя')
    Lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    Middle_name = models.CharField(max_length=100, verbose_name='Отчество')
    School = models.IntegerField(verbose_name='Школа')
    Class = models.IntegerField(verbose_name='Класс')
    published = models.DateField('Дата записи', null=True)

    class Meta:
        verbose_name = 'Импорт'
        verbose_name_plural = 'Импорт'
        ordering = ['-published']


class Desktop(Device):
    pass