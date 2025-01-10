from django import forms # 장고제공 폼 모듈
from .models import Product # 사용자 정의 모델 클래스

# 폼클래스 구성
# class ProductForm(forms.Form) : #일반 Form 클래스 상속
class ProductForm(forms.ModelForm) : # model 과 연동되는 form  클래스 상속
    class Meta:
        model = Product
        fields = ( #Product 모델 필드 중 form에 포함할 필드 나열
            'prdno',
            'prdname',
            'prdprice',
            'prdmaker',
            'prdcolor',
            'ctgno'
        )
        labels = {
            'prdno':'상품번호',
            'prdname':'상품명',
            'prdprice':'상품가격',
            'prdmaker':'제조사',
            'prdcolor':'색상',
            'ctgno':'카테고리'           
        }
