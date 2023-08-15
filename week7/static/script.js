let the_btn = document.getElementById("the_btn");
// 在表單提交時，檢查核取方塊的狀態
the_btn.addEventListener("click", function (event) {
    let checkbox = document.getElementById("checkbox");
    var text4Value = document.getElementById("text4").value;
    var text5Value = document.getElementById("text5").value;

    if (text4Value ===""||text5Value ===""){
        event.preventDefault(); // 阻止表單提交
        alert("請輸入資訊");
    }else if(!checkbox.checked) {
        event.preventDefault(); // 阻止表單提交
        alert("沒有勾選");
    }; 
});


