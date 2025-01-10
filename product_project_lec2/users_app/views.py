from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm # 등록된 user model통해서 db에 접근, id/pw 매칭 확인

# login 처리함수 (서버 -> 클라이언트)에게 로그인 증명서(cookie, session)를 전달
# 계속 요청을 보내면 유지되지만, 일정시간 이상 요청이 없는 증명서는 사라져서 재로그인 요청이 뜨는거임
from django.contrib.auth import login, logout 

# 표시되어 있는 함수는 login 되어 있지 않으면 함수처리 불가
# settings.py에 설정해놓은 LOGIN_URL로 돌아가줌
from django.contrib.auth.decorators import login_required

from .forms import CustomerCreationForm
from .forms2 import UserForm

from .models import User
# Create your views here.
# user model과 대응되어서 id, pw 유효성을 확인하기위한 입력 form을 제공되어지는 걸 쓰고
# 로그인 여부 처리하는 처리기능을 직접 구현
def sign_in(request):
    # post 방식 요청이면 로그인 여부 판단
    # 로그인 되면 index 페이지로
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST) 
        # form 객체 변수는 클라이언트로부터 전송된 id/pw 값을 갖고 있는 form 객체변수
        # id/pw가 틀리면 입력했던 데이터를 포함한 폼이 html 탬플릿으로 전송

        if form.is_valid(): # form -> users model -> db접근해서 id/pw 유효성 검증
            # id/pw가 맞으면
            login(request, form.get_user()) # 로그인 진행(set cookie, session)
        return redirect("index")  # 올바른 호출
    else : # get 방식 요청이면 빈 로그인 폼을 전달
        form = AuthenticationForm()

    # get 방식 요청이면 빈 로그인 폼을 전달    
    return render(request, "users_app/sign_in.html", {"form":form})
def sign_in(request):
    # post 방식 요청이면 로그인 여부 판단
    # 로그인 되면 index 페이지로
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST) 
        # form 객체 변수는 클라이언트로부터 전송된 id/pw 값을 갖고 있는 form 객체변수
        # id/pw가 틀리면 입력했던 데이터를 포함한 폼이 html 탬플릿으로 전송

        if form.is_valid(): # form -> users model -> db접근해서 id/pw 유효성 검증
            # id/pw가 맞으면
            login(request, form.get_user()) # 로그인 진행(set cookie, session)
        return redirect("index")  # 올바른 호출
    else : # get 방식 요청이면 빈 로그인 폼을 전달
        form = AuthenticationForm()

    # get 방식 요청이면 빈 로그인 폼을 전달    
    return render(request, "users_app/sign_in.html", {"form":form})
        
def sign_out(request):
    logout(request)
    return redirect("index")

# 회원가입 처리 : 
def sign_up(request):
    # {1} 장고 계정 생성 폼을 이용해서 사용자 custom form 생성
    form = CustomerCreationForm()
    if request.method == "POST" :
    # {2} 회원가입정보 -> form정보로 변환 -> model에 전송 -> db접근 저장
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("sign_in")
    return render(request, "users_app/sign_up.html", {"form":form})

def sign_up2(request):
    if request.method=="POST": # 회원가입처리 블록
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        user_name=request.POST["user_name"]
        user_phone=request.POST["user_phone"]
        user_address=request.POST["user_address"]
        # 전달받은 데이터를 model을 이용해서 회원가입 형태로 변환하여 처리
        # 장고의 회원가입은 create user라는 기능을 이용하도록 가이드하고 있음
        # form에 create 기능을 생성 또는 model을 이용한 create_user를 활용
        # 어찌되었든 회원정보를 암호화를 해야함

        # create user는 컬럼 추가 매개변수가 3개만 가능, 3개는 첫 추가
        # 이거 "순서" 주의, db에 입력된 컬럼순으로 해줘야함, 기본필드 이후에 추가필드
        user = User.objects.create_user(username, password, email)
        # -> 나머지는 속성으로 추가
        user.user_name = user_name
        user.user_phone = user_phone
        user.user_address = user_address

        user.save() # 폼이 아니라 모델을 직접 db에 save하는 형태
        return redirect("sing_in") # 로그인 하도록 유도하기 위해서 
    else: # 회원가입 from을 출력해줘야하는 블록
        form = UserForm()
    return render(request, "users_app/sign_up2.html", {"form":form})