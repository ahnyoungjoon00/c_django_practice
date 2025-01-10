$(document).ready(function(){
    $('#get_data_btn').on('click', function(){
        $.ajax({ //json 형식으로 전달
            url:"/product/ajax/data/",//서버측 요청 url(http://127.0.0.1:8000/product/ajax/data)
            datatype:'json',
            success:function(result){
                //ajax 요청 성공시 처리할 내용
                console.log(result);
                console.log(result.name);
                //반환된 result를 dom의 result_box에 출력
                $('#result_box').text(result.name) ;
            },
            error:function(){
                //ajax 요청 실패시 오류처리 내용
                alert("오류발생");
            },
            complete:function(){
                //완료되었을 대 처리 내용
            }
        }); //ajax끝
     }//click 처리 함수 끝
    );//on 끝
 }//ready 처리 함수끝
);//ready 끝