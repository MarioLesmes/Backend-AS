# Generated by Django 4.0.5 on 2022-07-18 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0017_alter_as_matorganica_alter_as_aluminiohidr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='as',
            name='MatOrganica',
        ),
    ]
