from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken 

from django.shortcuts import get_object_or_404

from users.models import User
from users.api.serializers import ClienteSerializer, TecnicoSerializer, AdministradorSerializer

class UsersViewSet(GenericViewSet):
  queryset = User.objects.filter(is_active= True)

  @action(detail=False, methods=['post'])
  def registrar_cliente(self, request):
    data = request.data
    cliente_serializer = ClienteSerializer(data= request.data, many= False)
    if cliente_serializer.is_valid():
      user = cliente_serializer.save()
      refresh = RefreshToken.for_user(user)
      return Response({
        'message':'Registro exitoso.',
        'refresh': str(refresh),
        'access': str(refresh.access_token)
      }, status=status.HTTP_201_CREATED)
    return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  

  



   