from django.db import models


class Aboutt(models.Model):
    zp = models.IntegerField('Заработная плата')
    trebovan = models.CharField('Требования', max_length=500)
    bonus = models.CharField('Бонусы', max_length=500)
    special = models.CharField('Специальность', max_length=500)
    navki = models.CharField('Ключевые навыки', max_length=500)
    o_kompani = models.CharField('О кампании', max_length=1000)
    number = models.CharField('Телефон', max_length=20)
    date = models.DateTimeField('Дата отправки', null=True, blank=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-date']