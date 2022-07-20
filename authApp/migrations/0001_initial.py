# Generated by Django 4.0.5 on 2022-07-05 01:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 7, 4, 20, 35, 9, 635123))),
                ('MatOrganica', models.DecimalField(decimal_places=3, default=2, max_digits=8)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('pH', models.DecimalField(decimal_places=4, max_digits=6)),
                ('fosforo', models.DecimalField(decimal_places=4, max_digits=6)),
                ('azufre', models.DecimalField(decimal_places=4, max_digits=6)),
                ('aluminioHidr', models.DecimalField(decimal_places=4, max_digits=6)),
                ('cice', models.DecimalField(decimal_places=4, max_digits=6)),
                ('conductividad', models.DecimalField(decimal_places=4, max_digits=6)),
                ('calcio', models.DecimalField(decimal_places=4, max_digits=6)),
                ('magnesio', models.DecimalField(decimal_places=4, max_digits=6)),
                ('potasio', models.DecimalField(decimal_places=4, max_digits=6)),
                ('sodio', models.DecimalField(decimal_places=4, max_digits=6)),
                ('hierro', models.DecimalField(decimal_places=4, max_digits=6)),
                ('cobre', models.DecimalField(decimal_places=4, max_digits=6)),
                ('manganeso', models.DecimalField(decimal_places=4, max_digits=6)),
                ('zinc', models.DecimalField(decimal_places=4, max_digits=6)),
                ('boro', models.DecimalField(decimal_places=4, max_digits=6)),
                ('balance', models.IntegerField(default=0)),
                ('isActive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AS', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]