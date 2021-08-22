from django.db.models import query_utils
from django.shortcuts import render
from rest_framework import status, generics
from .models import UserComments
from .serializers import UserCommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserCommentsApiViewAll(generics.ListAPIView):
    serializer_class = UserCommentsSerializer
    queryset = UserComments.objects.all()
       

class UserCommentsApiViewLatest(generics.ListAPIView):
    serializer_class = UserCommentsSerializer
    queryset= UserComments.objects.order_by().order_by('timeStamp', '-created_at').distinct('timeStamp')
       
    
class UserCommentsApiViewPost(APIView):
    serializer_class = UserCommentsSerializer
    def post (self, request, format=None): 
        requestData = self.serializer_class (data = request.data)
        if requestData.is_valid(): 
            userCommentObj = UserComments(username = requestData.data.get('username'), comment = requestData.data.get('comment'), timeStamp =requestData.data.get('timeStamp'))
            userCommentObj.save()
            return Response(UserCommentsSerializer(userCommentObj).data, status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


