from authApp.models.aS             import AS
from rest_framework                import serializers

class ASSerializer(serializers.ModelSerializer):
    class Meta:
        model  = AS
        fields = ['Materia_Organica', 'Latitud', 'Longitud', 'pH', 'Fosforo', 
                  'Azufre', 'Aluminio_Hidrogeno', 'CICE', 'Conductividad', 'Calcio', 
                  'Magnesio', 'Potasio', 'Sodio','Hierro', 'Cobre', 'Manganeso',
                  'Zinc', 'Boro']
