from authApp.models.user            import User
from authApp.models.aS              import AS
from rest_framework                 import serializers
from .aSSerializer                  import ASSerializer

class UserSerializer(serializers.ModelSerializer):
    aS = ASSerializer()
    class Meta: 
        model  = User
        fields = ['id', 'username','password','aS']

    def create(self, validated_data):
        aSData     = validated_data.pop('aS')
        userInstance    = User.objects.create(**validated_data)
        AS.objects.create(user=userInstance, **aSData)
        return userInstance

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        aS      = AS.objects.get(user=obj.id)
        return {
            "id"        : user.id,
            "username"  : user.username,
            "aS" : {
                "id"                : aS.id,
                "Materia_Organica"  : aS.Materia_Organica,
                "Latitud"           : aS.Latitud,
                "Longitud"          : aS.Longitud,
                "pH"                : aS.pH,
                "Fosforo"           : aS.Fosforo,
                "Azufre"            : aS.Azufre,
                "AluminioHidr"      : aS.Aluminio_Hidrogeno,
                "CICE"              : aS.CICE,
                "Conductividad"     : aS.Conductividad,
                "Calcio"            : aS.Calcio,
                "Magnesio"          : aS.Magnesio,
                "Potasio"           : aS.Potasio,
                "Sodio"             : aS.Sodio,
                "Hierro"            : aS.Hierro,
                "Cobre"             : aS.Cobre,
                "Manganeso"         : aS.Manganeso,
                "Zinc"              : aS.Zinc,
                "Boro"              : aS.Boro,
            }
        }
