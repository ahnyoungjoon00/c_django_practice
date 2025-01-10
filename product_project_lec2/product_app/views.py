from django.shortcuts import render, get_object_or_404,redirect
from .models import Product #product 테이블 구성 model 클래스
import pandas as pd 
from .forms import ProductForm
from django.db.models import Q #복잡한 조건은 생서하게 도와주는 클래스객체
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request) :
    return render(request, 'product_app/index.html')

# #상품정보 조회
# def product_list(request) :
#     # django_db product 테이블에서 모든 레코드 추출 후 템플릿에 전달
#     # 장고 orm 사용 : model 사용 모델class.objects.all() -> select * from 테이블
#     products = Product.objects.all() # 기본키 기준 오름차순정렬
#     # products 변수는 queryset dict 형식 -> 템플릿에 사용가능
#     # 서버 터미널에서 db에서 전송된 데이터 확인
#     print(products) # object 형태로 출력
#     print(Product.objects.values()) #db 레코드는 딕셔너리로 구성되고 전체 레코그다 리스트에 담겨있음
#     return render(request,'product_app/product_list.html',{'products':products})

#문자열 컬럼인 prdno를 수치형으로 변경 정렬
def product_list(request) :
    products = Product.objects.all() 
    #print(Product.objects.values()) 
    # queryset ->리스트변수 
    prd_list=[]
    for prd in products.values() :
        prd_list.append(prd)
    #print(prd_list)
    df=pd.DataFrame.from_dict(prd_list)
    ##print(df)
    df['prdno']=df['prdno'].astype(int) # 컬럼 타입 변환 함수(column.astype(변경할 타입명))
    df=df.sort_values(by=['prdno'],ascending=[True])
    products_dict=df.to_dict('records')
    print(products_dict)
    return render(request,'product_app/product_list.html',{'products':products_dict})

# 상세 상품 조회
# 전달받은 prdno(기본키)에 해당되는 1개 상품 데이터를 추출 -> 템플릿에 전송
def product_detail(request, pk) :
    # get_object_or_404(모델, 검색조건(pk)) : import 해서 사용
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product_app/product_detail.html',{'product':product})

# 상품 등록 처리
# 요청 : get 방식 -> 입력 폼 전달(템플릿 렌더링), 상품등록 메뉴를 클릭할때
# 요청 : post 방식 -> form 전송 데이터 유효성 검사 한 후에 db에 insert 후 상품조회 컨텐츠로 전환
#       데이터 입력 후 완료버튼을 클릭하면
@login_required
def product_insert(request) :
    # (1) 요청이 POST인지 확인하고
    if request.method == "POST" :
        #(2) 폼 데이터의 내용을 변수에 저장(폼클래스 형식으로 저장)
        form = ProductForm(request.POST) # 폼데이터로 변환됨
        #(3) Django form 의 기본 기능인 is_valid() 사용해서 데이터 유효성 확인
        if form.is_valid():
            # 유효성 위배사항이 없으면 form을 통해 저장(save) : commit 되지 않은 상태
            #(4) form.save()통해서 commit되지 않은 insert 진행->결과 변수에 저장
            product = form.save(commit=False)
            #(5) db에 반영
            product.save()
            #(6) 저장확인 위해서 상품조회 화면으로 이동
            return redirect('product_list')

    else : #get 방식 요청이면
        form = ProductForm() #사용자 정의 클래스의 생성자함수:입력폼 객체가 생성됨
    return render(request, 'product_app/product_form.html',{'form':form}) #get 방식 요청일때만 동작, 단 post 방식일 때 저장불가능한 데이터일 경우  동작

# 상품정보 수정
@login_required
def product_update(request, prdno) :
    #(1) 전달받은 prd_no의 데이터를 모델 통해서 db에서 select
    product = get_object_or_404(Product, pk=prdno)
       # (2) 요청이 POST인지 확인하고
    if request.method == "POST" :
        #(3) 폼 데이터의 내용을 변수에 저장(폼클래스 형식으로 저장)
        #전송된 데이터는 기존 모델통해서 db에서 select된 data와 연관있다(update)
        form = ProductForm(request.POST,instance=product) # 폼데이터(폼객체)로 변환됨
        #(4) Django form 의 기본 기능인 is_valid() 사용해서 데이터 유효성 확인
        if form.is_valid():
            # 유효성 위배사항이 없으면 form을 통해 저장(save) : commit 되지 않은 상태
            #(5) form.save()통해서 commit되지 않은 update 진행->결과 변수에 저장(form에 연결된 모델객체에 저장 후 반환)
            product = form.save(commit=False)
            #(6) db에 반영
            product.save()
            #(7) 저장확인 위해서 상품조회 화면으로 이동
            return redirect('product_list')

    else : #get 방식 요청이면
        form = ProductForm(instance=product) #product에 저장된 레코드 값들이 각 form의 필드의 value로 매칭됨
    # db에서 select된 데이터가 저장된 form    
    return render(request, 'product_app/product_update.html',{'form':form})

# 상품 삭제
@login_required
def product_delete(request, prdno):
    #기본키 컬럼값이 prdno값에 해당하는 레코드를 추출해서 model 객체에 저장(queryset)
    product = get_object_or_404(Product, pk=prdno)

    #model 객체인 queryset 변수(product)통해서 delete()
    product.delete() #상품데이터 삭제

    #상품 조회화면으로 이동(포워딩)
    return redirect('product_list')

# 검색창 열기
def product_search_form(request) :
    return render(request, 'product_app/product_search_form.html')

# 검색 쿼리 수행
def product_searchres(request) :
    if request.method=='POST' :
        type=request.POST['type'] #검색기준필드
        keyword=request.POST['keyword']#검색기준매칭값
        print(type, keyword)
        #prdname 이나 padmaker 필드의 값이 keyword값을 포함하면 true로 설정 후 필터링(select)
        prd_list= Product.objects.filter(Q(prdname__contains=keyword)|Q(prdmaker__contains=keyword))
        return render(request, 'product_app/product_search_form.html',{'prd_list':prd_list})

# ajax 연습을 위한 템플릿 처리    
def ajax_test(request) :
    return render(request, 'product_app/ajax_test2.html')

# json 형식으로 데이터만 전송(요청한 클라이언트 시스템에게 응답(Response))
# json 형식 : dict 형식
def get_data(request) :
    data = {'name' : '홍길동'} 
    return JsonResponse(data) # json 형식의  데이터를 클라이언트에게 전송

# 검색창 열기
def product_search_form2(request) :
    return render(request, 'product_app/product_search_form2.html')

# 검색 쿼리 수행
# ajax 이용해 비동기 요청 시 전달할 페이지 렌더링
# html 데이터를 ajax 요청 브라우저에 전달->ajax success function(result)로 html데이터를 전달
def product_searchres2(request) :
    if request.method=='POST' :
        type=request.POST['type'] #검색기준필드
        keyword=request.POST['keyword']#검색어
        print(type, keyword)
        # 검색 조건에 따른 검색 쿼리 작성, 검색조건값은 prd_name 아니면 prd_maker
        if type == 'prd_name' :
            prd_list = Product.objects.filter(Q(prdname__contains=keyword)) # select * from product where prdname like 'keyword값'
        elif type == 'prd_maker' :
            prd_list = Product.objects.filter(Q(prdmaker__contains=keyword))# select * from product where prdmaker like 'keyword값'
        else : #검색조건이 넘어오지 않으면 
            prd_list= Product.objects.filter(Q(prdname__contains=keyword)|Q(prdmaker__contains=keyword))           


        #prdname 이나 padmaker 필드의 값이 keyword값을 포함하면 true로 설정 후 필터링(select)
        #prd_list= Product.objects.filter(Q(prdname__contains=keyword)|Q(prdmaker__contains=keyword))
        return render(request, 'product_app/product_search_result.html',{'prd_list':prd_list})