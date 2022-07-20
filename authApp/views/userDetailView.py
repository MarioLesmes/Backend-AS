from django.conf                                import settings
from rest_framework                             import generics, status
from rest_framework.response                    import Response
from rest_framework.permissions                 import IsAuthenticated
from rest_framework_simplejwt.backends          import TokenBackend

from authApp.models.user                        import User
from authApp.serializers.userSerializer         import UserSerializer      

class UserDetailView(generics.RetrieveAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    permission_classes  =(IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        token         = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data    = token_backend.decode(token, verify=False)
        print(request)
        print(args)
        print(kwargs)
        if valid_data['user_id'] != kwargs['pk']:
            string_response ={'detail' : 'Acceso No Autotizado. '}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

class AnalisisSuelosUpdateView(generics.UpdateAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    permission_classes  = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("KWArgs:", kwargs)        
        token         = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data    = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['user']:
            string_response ={'detail' : 'Acceso No Autotizado. '}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)
        super().update(request, *args, **kwargs)
        return Response("Registro actualizado correctamente", status= status.HTTP_201_CREATED)

class AnalisisSuelosDeleteView(generics.DestroyAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    permission_classes  = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("KWArgs:", kwargs)        
        token         = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data    = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['user']:
            string_response ={'detail' : 'Acceso No Autotizado. '}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)
        
        super().destroy(request, *args, **kwargs)
        return Response("Registro eliminado correctamente", status= status.HTTP_201_CREATED)

