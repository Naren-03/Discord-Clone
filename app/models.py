from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True) #null = True means it can be empty allowed
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    updated = models.DateTimeField(auto_now=True) #auto_now take snapshot at every time we save 
    created = models.DateTimeField(auto_now_add=True)#auto_now_add take snapshot at only once time first time at created.


    class Meta:
        ordering = ['-updated','-created'] #using - it will reverse the order

    def __str__(self):
        return self.name
    

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #cascade means if we delete the room then message will completely deleted and set_null be store in database but not visible to user
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-updated','-created'] #using - it will reverse the order
        
    def __str__(self):
        return self.body