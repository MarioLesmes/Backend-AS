from django.db import models
from datetime  import datetime
from .user     import User

class AS(models.Model):
    id                  = models.AutoField(primary_key=True)
    user                = models.ForeignKey(User, related_name='AS', on_delete=models.CASCADE)
    Materia_Organica    = models.DecimalField('Mat_Organica',   max_digits =  15, decimal_places = 3)
    Latitud             = models.DecimalField('Latitud',            max_digits =  15, decimal_places = 12)
    Longitud            = models.DecimalField('Longitud',           max_digits =  15, decimal_places = 12)
    pH                  = models.DecimalField('pH',                 max_digits =  15, decimal_places = 4)
    Fosforo             = models.DecimalField('Fosforo',            max_digits =  15, decimal_places = 4)
    Azufre              = models.DecimalField('Azufre',             max_digits =  15, decimal_places = 4)
    Aluminio_Hidrogeno  = models.DecimalField('Aluminio_Hidrogeno', max_digits =  15, decimal_places = 4)
    CICE                = models.DecimalField('CICE',               max_digits =  15, decimal_places = 4)
    Conductividad       = models.DecimalField('Conductividad',      max_digits =  15, decimal_places = 4)
    Calcio              = models.DecimalField('Calcio',             max_digits =  15, decimal_places = 4)
    Magnesio            = models.DecimalField('Magnesio',           max_digits =  15, decimal_places = 4)
    Potasio             = models.DecimalField('Potasio',            max_digits =  15, decimal_places = 4)
    Sodio               = models.DecimalField('Sodio',              max_digits =  15, decimal_places = 4)
    Hierro              = models.DecimalField('Hierro',             max_digits =  15, decimal_places = 4)
    Cobre               = models.DecimalField('Cobre',              max_digits =  15, decimal_places = 4)
    Manganeso           = models.DecimalField('Manganeso',          max_digits =  15, decimal_places = 4)
    Zinc                = models.DecimalField('Zinc',               max_digits =  15, decimal_places = 4)
    Boro                = models.DecimalField('Boro',               max_digits =  15, decimal_places = 4)