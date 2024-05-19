from django.db import models
from django.contrib.auth.models import User
import string
import random
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q

def generate_token():
    return ''.join(random.choice(string.ascii_letters) for _ in range(8))

class Zabka(models.Model):
    localization = models.CharField(max_length=200, blank=False, null=True)
    token = models.CharField(max_length=10, blank=False, null=True, default=generate_token)
    name = models.CharField(max_length=10, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class VisitedZabkas(models.Model):
    zabka = models.ManyToManyField(Zabka)
    visitor = models.ForeignKey(User, on_delete = models.CASCADE)
    
class Achievements(models.Model):
    achievment_id = models.AutoField(primary_key=True)
    achievement_name = models.CharField(max_length=200, blank=False, null=True)

class AssignedAcievments(models.Model):
    achievement_owner = models.ForeignKey(User, on_delete = models.CASCADE)
    achievment_id = models.ForeignKey(Achievements, on_delete = models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class StoreComment(models.Model):
    store = models.ForeignKey('Zabka', on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    Ocena = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    #class Meta:
    #    constraints = [
    #        models.UniqueConstraint(fields=['store', 'user'], condition=Q(parent__isnull=True), name='unique_main_comment')
    #    ]

    def __str__(self):
        return f"Comment by {self.user.username} on {self.store.name} - Rating: {self.Ocena}"


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