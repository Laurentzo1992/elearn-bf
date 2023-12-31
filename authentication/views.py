from django.shortcuts import redirect, render
from authentication.models import UserManager, User
from authentication.serializers import UserRegistrationSerializer, UserSerializer, UserLoginSerilizer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import  login, logout, authenticate
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated




class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    
    def get_queryset(self):
        return User.objects.all()

    # Vue de connexion personnalisée
    def login_user(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        # Vérifiez les informations de connexion
        user = authenticate(request, email=email, password=password)
        
        if user:
            login(request, user)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Connexion refusée veuillez verifer vos identifiants'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
class UserLogout(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Déconnexion de l'utilisateur
        logout(request)
        return Response({"message": "Déconnexion réussie."}, status=status.HTTP_200_OK)
    
         

""" class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegistrationSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) """
        
        
        

            



