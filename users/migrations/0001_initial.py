# Generated by Django 3.2.16 on 2023-03-19 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateField(default=datetime.date.today, verbose_name='Data de cadastro')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('cep', models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua')),
                ('neighborhood', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('state', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sobrenome')),
                ('cpf', models.CharField(blank=True, max_length=15, null=True, verbose_name='CPF')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
