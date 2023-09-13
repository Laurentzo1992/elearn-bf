from rest_framework.serializers import ModelSerializer
from elearn.models import Matiere, Categorie, Cours, Enseignant, Apprenant

 
 
 
class MatiereSerializer(ModelSerializer):
 
    class Meta:
        model = Matiere
        fields = '__all__'
        
    
    
          
        
        
        
class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
        

        
        
class CoursSerializer(ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'