const targetForm = document.querySelector('.jss_content_form')
// 해당하는 클래스(.으로 시작)를 가져와서 선택 => textarea 선택
const counted_text = document.querySelector('.counted_text')
targetForm.addEventListener("keyup", function() {
    counted_text.innerHTML = targetForm.value.length
})
// 선택한 폼에 "keyup" 이벤트가 발생했을 때