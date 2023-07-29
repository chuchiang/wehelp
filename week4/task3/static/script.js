let the_btn = document.getElementById("the_btn");

// 在表單提交時，檢查核取方塊的狀態
the_btn.addEventListener("click", function (event) {
    let checkbox = document.getElementById("checkbox");
    if (!checkbox.checked) {
        event.preventDefault(); // 阻止表單提交
        alert("沒有勾選");
    }
});