from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Publisher
import pandas as pd
from .forms import BookForm
from django.db.models import Q

# Create your views here.
def index(request) :
    return render(request,'book_app/index.html')

#도서정보 조회서비스
def book_list(request) :
    books = Book.objects.all() #장고 자료형 query set dict,db 관련 속성 포함(외래키 등 사용가능)
    print(Book.objects.values())
    bk_list=[]
    for bk in books.values() :
        bk_list.append(bk)
    df= pd.DataFrame.from_dict(bk_list)
    df['bookno']=df['bookno'].astype(int)
    df = df.sort_values(by=['bookno'], ascending=[True])
    book_dict=df.to_dict('records') #python 자료형  dict, db 관련 속성 없음(외래키 등 사용 불가)
    return render(request,'book_app/book_list.html',{'books':books}) #템플릿에서 외래키 사용 가능
    #return render(request,'book_app/book_list.html',{'books':book_dict}) #템플릿에서 외래키 사용 불가

#도서상세정보 조회
def book_detail(request, bookno) :
    book = get_object_or_404(Book, pk=bookno) # db 속성 저장되어 있는 변수
    return render(request, 'book_app/book_detail.html', {'book':book})

#새로운 도서 등록
def book_insert(request) :
    if request.method == "POST" :
        form = BookForm(request.POST)
        if form.is_valid() :
            book = form.save(commit=False)
            book.save()
            return redirect('book_list')
    else :   
        form = BookForm()
    return render(request, 'book_app/book_form.html', {'form':form})

def book_update(request, bookno) :
    book = get_object_or_404(Book, pk=bookno)
    if request.method == "POST" :
        form = BookForm(request.POST,instance=book)
        if form.is_valid() :
            book = form.save(commit=False)
            book.save()
            return redirect('book_list')
    else : #get방식의 요청  
        form = BookForm(instance=book)
    return render(request, 'book_app/book_form.html', {'form':form})    

def book_delete(request, bookno) :
    book = get_object_or_404(Book, pk=bookno)
    book.delete()
    return redirect('book_list')

def book_search_form_a(request)  :
    pub_list = Publisher.objects.only('pubname') #출판사컬럼만 추출 : only() 특정컬럼추출시 사용
    return render(request, 'book_app/book_search_form_a.html',{'publist':pub_list})

def book_search_a(request) :
    pub_list = Publisher.objects.only('pubname') #출판사컬럼만 추출 : only() 특정컬럼추출시 사용
    if request.method == "POST" :
        type = request.POST['type']
        keyword = request.POST['keyword']

        if type == 'bookname' :
            book_list = Book.objects.filter(Q(bookname__contains=keyword))
        elif type == 'bookauthor' :
            book_list = Book.objects.filter(Q(bookauthor__contains=keyword))
        elif type == 'publisher' : # book 테이블에는 pubno(출판사번호)가 있음, keyword값은 pubname(출판사이름)
            book_list = Book.objects.filter(Q(pubno__pubname__contains=keyword)) #join 연산을 진행하게 됨(Book, Publisher)

    return render(request, 'book_app/book_search_form_a.html',{'book_list':book_list, 'publist':pub_list})


