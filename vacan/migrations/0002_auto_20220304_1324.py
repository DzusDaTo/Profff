# Generated by Django 3.2.7 on 2022-03-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacan', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacan',
            options={'ordering': ['-date'], 'verbose_name': 'Вакансии вывод', 'verbose_name_plural': 'Вакансии вывод'},
        ),
        migrations.AlterField(
            model_name='vacan',
            name='date',
            field=models.DateField(verbose_name='Дата размещения'),
        ),
        migrations.AlterField(
            model_name='vacan',
            name='zp',
            field=models.IntegerField(verbose_name='Заработная плата'),
        ),
    ]