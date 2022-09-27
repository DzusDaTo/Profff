# Generated by Django 3.2.6 on 2021-08-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0002_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('zip_code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=30)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]