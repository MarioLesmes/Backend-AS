# Generated by Django 4.0.5 on 2022-07-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0014_alter_as_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='as',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
