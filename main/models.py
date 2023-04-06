from django.db import models
from django.contrib.auth.models import User

class Gorev(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    baslik = models.CharField(max_length=250)
    aciklama = models.TextField(null=True, blank=True)
    bitis = models.BooleanField(default=False)
    eklenis = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.baslik
    
    class Meta:
        ordering = ['bitis']