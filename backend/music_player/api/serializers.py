from rest_framework import serializers
from .models import UserComments

class UserCommentsSerializer (serializers.ModelSerializer): 
    class Meta: 
        model =  UserComments
        fields = ('id','username','comment','timeStamp')
        
