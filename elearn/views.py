from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from elearn.models import Matiere, Categorie, Cours, Apprenant, Enseignant
from  django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.conf import settings
from elearn.serializers import CategorieSerializer, CoursSerializer, MatiereSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import  login, logout, authenticate, get_user_model
from django.views import View
from django.http import JsonResponse



class LoginView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully.'})
        else:
            return JsonResponse({'message': 'Invalid credentials.'}, status=401)
        
        
        
class LogoutView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({'message': 'Logged out successfully.'})
        else:
            return JsonResponse({'message': 'User is not authenticated.'}, status=401)

#api to create red delete and update Matiere objets
    
    
class MatiereViewset(ModelViewSet):
 
    serializer_class = MatiereSerializer
 
    def get_queryset(self):
        return Matiere.objects.all()
    
    
#api to create red delete and update Categorie objets 
    
class CategorieViewset(ModelViewSet):
 
    serializer_class = CategorieSerializer
 
    def get_queryset(self):
        return Categorie.objects.all()
    


#api to create red delete and update Cours objets
 
class CoursViewset(ModelViewSet):
 
    serializer_class = CoursSerializer
 
    def get_queryset(self):
        return Cours.objects.all()   
    
    
    
    
    
def home(request):
    return render(request, 'elearn/home.html')
    
    


    
    








