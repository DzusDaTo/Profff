# Generated by Django 3.2.7 on 2022-03-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220302_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='published',
            field=models.DateField(blank=True, verbose_name='Дата записи'),
        ),
    ]