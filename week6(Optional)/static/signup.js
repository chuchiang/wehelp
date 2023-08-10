let register = document.getElementById("register");
// 在表單提交時，檢查核取方塊的狀態
register.addEventListener("click", function (registerevent) {
    var text1Value = document.getElementById("text1").value;
    var text2Value = document.getElementById("text2").value;
    var text3Value = document.getElementById("text3").value;

    if (text1Value ===""||text2Value ===""||text3Value ==="") {
        registerevent.preventDefault(); // 阻止表單提交
        alert("請輸入資訊");
    }
});