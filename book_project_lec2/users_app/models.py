from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # 새로운 필드 (db컬럼)을 추가
    user_name=models.CharField(max_length=30)
    user_phone=models.CharField(max_length=20)
    user_address=models.CharField(max_length=200)

