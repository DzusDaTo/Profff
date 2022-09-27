# Generated by Django 3.2.9 on 2022-03-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutt',
            options={'ordering': ['-date'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AddField(
            model_name='aboutt',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки'),
        ),
        migrations.AlterField(
            model_name='aboutt',
            name='zp',
            field=models.IntegerField(verbose_name='Заработная плата'),
        ),
    ]
