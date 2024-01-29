from itertools import product
from django.db import models
# from django.contrib.auth.models import User
import datetime
import os
from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()

def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S") + '_'
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)
 
class User_Voice(models.Model):
  from_user_name=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='from_user_name')
  to_user_name=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='to_user_name')
  voice_file=models.FileField(upload_to=getFileName)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self):
    return f"{self.from_user_name}, {self.to_user_name}, {self.voice_file}"

class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=2500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    # return f"{self.name}, {self.description}, {self.created_at}"
    return self.name

  @property
  def get_audios(self):
     return Audio.objects.filter(category__root=(...))
  
class Audio(models.Model):
  # Catagory_name=models.ForeignKey(Catagory, on_delete=models.DO_NOTHING, related_name='Catagory_name')
  Catagory_name=models.ForeignKey(Catagory, on_delete=models.DO_NOTHING)
  name=models.CharField(max_length=150,null=False,blank=False)
  audio_file=models.FileField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=2500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self) :
    return f"{self.Catagory_name}, {self.name}, {self.audio_file}, {self.created_at}"

class Audio_User(models.Model): 
  # Audio_name=models.ForeignKey(Audio, on_delete=models.DO_NOTHING, related_name='Audio_name')
  # User_name=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='User_name')
  Audio_name=models.ForeignKey(Audio, on_delete=models.DO_NOTHING)
  User_name=models.ForeignKey(User, on_delete=models.DO_NOTHING)

  def __str__(self) :
    return f"{self.Audio_name}, {self.User_name}"
  
class Audio_Group(models.Model): 
  Audio_name=models.ForeignKey(Audio, on_delete=models.DO_NOTHING)
  Group_name=models.ForeignKey(Group, on_delete=models.DO_NOTHING)

  def __str__(self) :
    return f"{self.Audio_name}, {self.Group_name}"
