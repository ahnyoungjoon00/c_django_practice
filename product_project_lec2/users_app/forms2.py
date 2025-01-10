# dbms <-> model <-> forms <-> template <-> client 
# 의 구성으로 연결됨

from django import forms # 일반폼 생성시에 사용할
from .models import User

class UserForm(forms.ModelForm): # model form이고 uwer계정의 create user을 활용하는게 불가능해서 일일이 형식을 만들어줘야함
    class Meta:
        model = User 

        # 회원가입 시, 사용할 필드를 구성
        # django의 회원가입폼을 사용하지 않으려면 password 입력을 따로 요구해야함
        fields=(
            "username",
            "password",
            "email",
            "user_name",
            "user_phone",
            "user_address",
        )
        labels={
            "username":"ID",
            "password":"PW",
            "email":"E-mail",
            "user_name":"성명",
            "user_phone":"전화번호",
            "user_address":"주소",
        }