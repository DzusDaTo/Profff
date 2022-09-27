from django.db import models


class Resume(models.Model):
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    number = models.CharField('Номер телефона', max_length=30)
    city = models.CharField('Проживаете в городе/селе', max_length=50)
    dater = models.CharField('Дата рождения', max_length=20)
    gender = models.CharField('Пол', max_length=10)
    opat_rabot = models.CharField('Опыт работы', max_length=100)
    special = models.CharField('Специальность', max_length=100)
    o_sebe = models.CharField('О себе', max_length=500)
    obrazov = models.CharField('Образование', max_length=50)
    obraz_ucher = models.CharField('Образовательное учереждение', max_length=150)
    leanguage = models.CharField('Языки', max_length=100)
    komandirovka = models.CharField('Готовность к командировкам', max_length=50)
    zanyatost = models.CharField('Занятость', max_length=50)
    date = models.DateField('Дата отправки')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        ordering = ['-date']
