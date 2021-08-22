from django.urls import path, include
from .views import UserCommentsApiViewAll
from .views import UserCommentsApiViewLatest
from .views import UserCommentsApiViewPost
urlpatterns = [
    path('api/all', UserCommentsApiViewAll.as_view()), 
    path('api/latest', UserCommentsApiViewLatest.as_view()), 
    path('api/post', UserCommentsApiViewPost.as_view()), 
]
