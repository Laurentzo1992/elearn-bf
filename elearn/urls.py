from  . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from elearn.views import CategorieViewset, CoursViewset, MatiereViewset
from .views import LoginView

# Ici nous créons notre routeur
router = routers.SimpleRouter()

# Puis nous  déclarons une url basée sur le nom des model et des vues
# afin que l’url générée soit celle que nous souhaitons ‘/api/cour/’


urlpatterns = [
    path('api/', include(router.urls)),
]

