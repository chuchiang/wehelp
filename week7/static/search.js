let search = document.getElementById("searchBtn");

search.addEventListener("click", function () {
    let username = document.getElementById("searchName").value;;
    let url = 'http://127.0.0.1:3000/api/member?username='+ username.toString();
   
   //Fetch請求發送數據到python後端
   fetch(url)
   .then(function(response) {
    return response.json();
    })
    .then(function(data) {
    let result = document.getElementById("result");
    if (data["data"]!=null){
        let name=data["data"]["name"]
        let username=data["data"]["username"]
        console.log(username)
        result.innerHTML=name+"("+username+")"
    }else if(data["data"]==null) {
        result.innerHTML = "未找到會員訊息";
    }
   });
});

let replaceBtn = document.getElementById("replaceBtn");


replaceBtn.addEventListener("click", function () {
    let replaceName = document.getElementById("replaceName").value;;
    
   //Fetch請求發送數據到python後端
   fetch("/api/member", {
    method: "PATCH",
    body: JSON.stringify({
        name:replaceName
    }),
    headers: {
        'Content-type': 'application/json; charset=UTF-8', // 設定內容類型
    },
    })
    .then(function(response) {
        return response.json();
        })
        .then(function(data) {
            let replacResult = document.getElementById("replacResult");
            if (data["ok"]=="true"){
                replacResult.innerHTML="更新成功"
                let name=document.getElementById("name")
                name.innerHTML=replaceName+"，成功登入系統"
            }else{
                replacResult.innerHTML="更新失敗"
            }

    });

});