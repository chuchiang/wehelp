



// 返回一個 NodeList
let deleteConten = document.getElementsByClassName("delete");
 

// 使用迴圈遍歷每個元素
for (let i = 0; i < deleteConten.length; i++) {
    let button = deleteConten[i];
    let messageId = button.getAttribute("contentId"); 
// click時執行
    button.addEventListener("click", function () {
        let yes=confirm("你確定嗎?");
        if (yes){
            //Fetch請求發送數據到python後端
            fetch("/deleteMessage", {
                method: "POST",
                headers: {
                    'Content-Type': 'text/plain' // 設定內容類型為純文本
                },
                    body: messageId // 直接傳送數字
                })
                .then(response => response.text()) // 解析後端的回應
                .then(() => {
                    location.reload();//強制重新整理頁面
                });
        }
    });
}
