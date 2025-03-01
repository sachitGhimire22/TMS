from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return f'{self.user.username if self.user else "No User"} - {self.title[:5]}'

    