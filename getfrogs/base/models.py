from django.db import models

# Create your models here.

class Advocate(models.Model):
    username = models.CharField(max_length=50)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username #W bazie dzieki temu jak wejdziecie w admin page widac nazwy uzytkownikow a nie ID? w sumie nie wiem czy to ID ale no takie numerki w nawiasach są, takze chyba tak
    
