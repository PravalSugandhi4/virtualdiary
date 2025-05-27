from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class client(models.Model):
    STATUS_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'Inactive'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clientid=models.CharField(max_length=40,unique=True)
    name=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')
        

    def __str__(self):
        return f"{self.clientid} - {self.name} - {self.name} - {self.email}-------------------{self.status}"
class post(models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client}  - {self.created_at} "

