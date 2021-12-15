from django.db import models
from django.contrib.auth.models import User, AbstractUser 
import uuid

# Create your models here.
class User(AbstractUser):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NaN', 'Rather not to say'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=100, default='No address inserted')
    personal_mobile_no = models.BigIntegerField(null=False,default=0)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=gender_choices, default='NaN')
    guardain_name = models.CharField(max_length=50, default='Father name ?')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.username
