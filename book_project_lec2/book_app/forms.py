from django import forms
from .models import Book, Publisher

#ModelForm  클래스 상속 받음
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'bookno',
            'bookauthor',
            'bookprice',
            'bookdate',
            'bookstock',
            'pubno'
       )
        
        labels = {
            'bookno':'도서번호',
            'bookauthor':'도서명',
            'bookprice':'가격',
            'bookdate':'출판일',
            'bookstock':'재고',
            'pubno':'출판사'            
        }

