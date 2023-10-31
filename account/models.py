from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(User):
    
    otp = models.IntegerField(blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.username
    