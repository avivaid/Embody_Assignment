from django.db import models

class UserComments(models.Model): 
    username  = models.CharField(max_length=50,  null = False)
    comment  = models.CharField(max_length=5000, null = False )
    timeStamp  = models.CharField(max_length=4,null =False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    