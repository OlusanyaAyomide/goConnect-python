from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username=models.CharField(max_length=50)
    memory=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.username

class MessageModel(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="message")
    createdAt=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self):
      return self.type + " " + self.user.username




