from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# AbstractUser 상속
class User(AbstractUser) :
    # AbstractUser의 모든 필드가 상속되고, 현재 클래스에서 추가하는 필드가 확장, 포함
    # 새로운 필드 추가
    user_name=models.CharField(max_length=30) # 이름 저장 필드
    user_phone=models.CharField(max_length=30) # 번호 저장 필드
    user_address=models.CharField(max_length=30) # 주소 저장 필드
    # django에서 기본적으로 제공하는 User 기능 전부를 포함하고 + 새로운 필드 추가임