# Generated by Django 3.2.7 on 2022-03-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_shipment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shipment',
            options={'ordering': ['-published'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AddField(
            model_name='shipment',
            name='published',
            field=models.DateField(verbose_name='Дата записи'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Тема мероприятия'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='ФИО'),
        ),
    ]
