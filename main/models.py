from django.db import models


class Shipment(models.Model):
    last_name = models.CharField('ФИО', max_length=50)
    first_name = models.CharField('Тема мероприятия', max_length=50)
    Email = models.CharField('Email', max_length=50)
    school = models.CharField('Название школы и №', max_length=50)
    age = models.CharField('Возраст', max_length=50)
    grade = models.CharField('Класс', max_length=50)
    fio = models.CharField('ФИО родителя', max_length=50)
    number_fio = models.CharField('Телефон родителя', max_length=50)
    published = models.DateField('Дата записи', blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-published']


