# Generated by Django 3.2.7 on 2022-01-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zp', models.CharField(max_length=50, verbose_name='Заработная плата')),
                ('trebovan', models.CharField(max_length=500, verbose_name='Требования')),
                ('bonus', models.CharField(max_length=500, verbose_name='Бонусы')),
                ('special', models.CharField(max_length=500, verbose_name='Специальность')),
                ('navki', models.CharField(max_length=500, verbose_name='Ключевые навыки')),
                ('o_kompani', models.CharField(max_length=1000, verbose_name='О кампании')),
                ('number', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
