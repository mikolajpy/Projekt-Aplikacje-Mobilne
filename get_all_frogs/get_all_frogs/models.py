from django.db import models
from django.contrib.auth.models import User


class Zabka(models.Model):
    localization = models.CharField(max_length=200, blank=False, null=True)

class Token(models.Model):
    zabka = models.ManyToManyField(Zabka, blank=False, related_name="Zabka_place")
    visitor = models.ForeignKey(User, on_delete = models.CASCADE)
    value = models.CharField(max_length=10, blank=False, null=True) 

class Achievements(models.Model):
    achievement_owner = models.ForeignKey(User, on_delete = models.CASCADE)
    achievement_name = models.CharField(max_length=200, blank=False, null=True)

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