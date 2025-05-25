from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
    bio = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    picture = models.ImageField(null=True, blank=True, upload_to='profile_images/', default='avatar.png')
    # role 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

# class StudentProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     bio = models.CharField(max_length=200)
#     picture = models.ImageField(null=True, blank=True, upload_to='profile_images/', default='avatar.png')
    
#     def __str__(self):
#         return self.user.username
    

class Course(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title