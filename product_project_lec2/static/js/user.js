const pattern = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-za-z0-9\-]+/;

function test(){
    // 비밀번호 입력, 입력 확인 객체 참조 변수 호츌&확인
    var p1 = document.getElementById("password");
    var p2 = document.getElementById("password2");
    // email 객체 참조 변수 호츌&확인
    var email = document.getElementById("email");
    // submit 처리를 위해 form 객체 참조 변수
    var frm= document.getElementById("joinform");

    // pw는 8글자 이상
    if(p1.value.length<8){
        alert("비밀번호는 8자 이상으로 이루어져야합니다.")
        p1.value = "";
        p2.value = "";
        p1.focus();
        return false;
    }
    if(p1.value != p2.value){
        alert("비밀번호가 불일치합니다.");
        p1.value = "";
        p2.value = "";
        p1.focus();
        return false;
    }else{
        alert("적합한 비밀번호입니다.");
    }

    if(pattern.test(email.value) == false){
        alert("이메일 형식 오류");
        email.value="";
        email.focus();
        return false;
    }else{
        frm.submit();
    }
} // test 끝