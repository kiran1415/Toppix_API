from rest_framework import serializers
from .models import ( 
    Toppix,
    Tags,
    SubCategory,
    Category)




class ToppixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toppix
        fields = '__all__'