from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Usuario
from .serializers import UsuarioSerializer
from django.contrib.auth.hashers import make_password  

class UsuarioList(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['contraseña'] = make_password(request.data['contraseña']) 
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return None

    def get(self, request, pk):
        usuario = self.get_object(pk)
        if usuario:
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        usuario = self.get_object(pk)
        if usuario:
            request.data['contraseña'] = make_password(request.data['contraseña'])  
            serializer = UsuarioSerializer(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        usuario = self.get_object(pk)
        if usuario:
            usuario.delete()
            return Response({"message": "Usuario eliminado"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
