from django.db import models


class Vacan(models.Model):
    zp = models.IntegerField('Заработная плата')
    trebovan = models.CharField('Требования, Опыт работы, Занятость', max_length=500)
    bonus = models.CharField('Бонусы', max_length=500)
    navki = models.CharField('Навыки, Языки, Образование, Вод.Уд', max_length=500)
    o_kompanii = models.CharField('О кампании, Название компании, Город', max_length=1000)
    number = models.CharField('Телефон', max_length=20)
    special = models.CharField('Специальность', max_length=100)
    date = models.DateField('Дата размещения')

    def str(self):
        return self.special

    class Meta:
        verbose_name = 'Вакансии вывод'
        verbose_name_plural = 'Вакансии вывод'
        ordering = ['-date']
