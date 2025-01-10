# dbms <-> model <-> forms <-> template <-> client 
# 의 구성으로 연결됨

from django import forms # 일반폼 생성시에 사용할
from django.contrib.auth.forms import UserCreationForm # 사용자 계정과 관련된 폼 
from django.contrib.auth import get_user_model # 현재 프로젝트 구성에 연결된 USER_MODEL을 반환

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model() # settings.py에 등록된 AUTH_USER_MODEL을 사용
        
        # 회원가입 시, 사용할 필드를 구성
        fields=(
            "username",
            "email",
            "user_name",
            "user_phone",
            "user_address",
            # password는 굳이 추가하지 않아도 자동으로 넣어서 구성해줌
        )
        labels={
            "username":"ID",
            "email":"E-mail",
            "user_name":"성명",
            "user_phone":"전화번호",
            "user_address":"주소",
        }