let the_btn = document.getElementById("the_btn");
the_btn.addEventListener("click", function (event) {

    let checkbox = document.getElementById("checkbox");

    if (!checkbox.checked) {
        event.preventDefault(); // 阻止表單提交
        alert("Please check the checkbox first");
    }

});