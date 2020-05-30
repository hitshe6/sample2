from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    username= models.CharField(max_length = 122)

    def __str__(self):
        return self.username 


class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    text= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

