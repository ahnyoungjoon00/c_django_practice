$(document).ready(function(){
    $('#prdSearchFrm2').on('submit', function(){
        //submit 이벤트 기본 기능으로 페이지 새로고침
        //이벤트의 기본 기능 중단시키는 함수        
        event.preventDefault();

        //폼에 입력한 값들을 전송데이터로 변환
        //쿼리스트링방식으로 구성 : csrftoken=xxxxxxx&type=prd_Name&keyword=노트북
        //serialize() 제이쿼리 함수 : dom 함수
        var formData = $(this).serialize(); //현재 dom의 form 태그 내의 모든 폼 객체값을 쿼리스트링으로 구성
        $.ajax({
            type:"post", //post 방식 요청
            url:"http://127.0.0.1:8000/product/search/result2/",
            data:formData,
            success:function(result){
                console.log(result);
                //반환된 결과를 searchResultBox인 div 에 삽입(html태그로 삽입)
                $('#searchResultBox').html(result);
            },
            error:function(){
                alert("전송실패");
            },
            complete:function(){

            }
        });//ajax 끝
    });//on 끝
});//ready 끝