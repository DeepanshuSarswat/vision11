# Generated by Django 3.2.12 on 2022-03-15 14:02

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('vision_credits', models.FloatField(default=0)),
                ('currency_type', models.CharField(choices=[('vision coins', 'vision coins'), ('vision candies', 'vision candies')], default=('vision candies', 'vision candies'), max_length=50)),
                ('gender_type', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('country', models.CharField(max_length=100)),
                ('is_adult', models.BooleanField(default=False, verbose_name='Adult_status')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff_status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='super_user_status')),
                ('aadhar_image', models.FileField(blank=True, null=True, upload_to='others')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
