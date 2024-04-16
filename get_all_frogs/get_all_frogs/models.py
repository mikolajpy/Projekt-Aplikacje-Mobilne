from django.db import models
from django.contrib.auth.models import User
import string
import random

def generate_token():
    return ''.join(random.choice(string.ascii_letters) for _ in range(8))

class Zabka(models.Model):
    localization = models.CharField(max_length=200, blank=False, null=True)
    token = models.CharField(max_length=10, blank=False, null=True, default=generate_token)

class VisitedZabkas(models.Model):
    zabka = models.ManyToManyField(Zabka, blank=False, related_name="Zabka_place")
    visitor = models.ForeignKey(User, on_delete = models.CASCADE)
    
class Achievements(models.Model):
    achievment_id = models.AutoField(primary_key=True)
    achievement_name = models.CharField(max_length=200, blank=False, null=True)

class AssignedAcievments(models.Model):
    achievement_owner = models.ForeignKey(User, on_delete = models.CASCADE)
    achievment_id = models.ForeignKey(Achievements, on_delete = models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    



# class Chat(models.Model):
#     participant_1 = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'participant_1')
#     participant_2 = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'participant_2')

#     recent_message_owner = models.TextField(blank = True, null = True, default = '')
#     recent_message = models.TextField(blank = True, null = True, default = '')

#     created = models.DateTimeField(auto_now = True)
#     updated = models.DateTimeField(auto_now_add = True)
    
#     class Meta:
#         ordering = ['-created', '-updated']


# class Message(models.Model):
#     chat = models.ForeignKey(Chat, on_delete = models.CASCADE)
#     owner = models.ForeignKey(User, on_delete = models.CASCADE)

#     body = models.TextField(blank = False, null = False)

#     created = models.DateField(auto_now = True)
#     updated = models.DateTimeField(auto_now_add = True)

#     class Meta:
#         ordering = ['-created', '-updated']