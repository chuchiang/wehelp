console.log("== task1 ==")
function findAndPrint(messages){

    for(let i =0; i < Object.keys(messages).length; i++){ //跑全部內容
        let key = Object.keys(messages)[i];//宣告key=名字
        let value = messages[key];//宣告value=內容
        if (value.includes("18")){
            console.log(key)
        }else if (value.includes("college student")){
            console.log(key)
        }else if (value.includes("legal age")){
            console.log(key)
        }else if (value.includes("vote")){
            console.log(key)
        }
      }

}
    findAndPrint({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
    });
console.log("== task2 ==")
function calculateSumOfBonus(data) {
    let salary1 = 0;
    let salary2 = 0;
    let salary3 = 0;

    //先將各別薪水拉出來，轉成數字型別
    for (let i = 0; i < data.employees.length; i++) {

        if (typeof data.employees[i].salary === "string" && data.employees[i].salary.indexOf("USD") > -1) {
            salary1 = data.employees[i].salary.replace("USD", "") * 30;
        }

        else if (typeof data.employees[i].salary === "string") {
            salary2 = parseInt(data.employees[i].salary.replace(",", ""));
        }
        else {
            salary3 = parseInt(data.employees[i].salary);
        }
    }

    //依照各別狀況來看BOUNS 要多少
    let bouns1 = 0;
    let bouns2 = 0;
    let bouns3 = 0;
    for (let i = 0; i < data.employees.length; i++) {
        if (data.employees[i].performance.includes("above average")) {
            bouns1 = salary1 * 0.09;
        }
        else if (data.employees[i].performance.includes("below average")) {
            bouns2 = salary2 * 0.04;
        }
        else if (data.employees[i].role.includes("CEO")){
            bouns3 = salary3 * 0.08;
        }
    }
   
    let bounsTotal = bouns1+bouns2+bouns3;
    console.log(bounsTotal);

}
calculateSumOfBonus({
    "employees":[
    {
    "name":"John",
    "salary":"1000USD",
    "performance":"above average",
    "role":"Engineer"
    },
    {
    "name":"Bob",
    "salary":60000,
    "performance":"average",
    "role":"CEO"
    },
    {
    "name":"Jenny",
    "salary":"50,000",
    "performance":"below average",
    "role":"Sales"
    }
    ]
    }); // call calculateSumOfBonus function

console.log("== task3 ==")
function func(...data) {
    function getSecondName(data) {
      let wordCounts = {};//字出現次數
      let result = [];//一個陣列
  
      for (let i = 0; i < data.length; i++) {
        let name = data[i];
        let secondName = name[1]; // 得到每個字串的第二個字
        if (wordCounts[secondName]) {
          wordCounts[secondName]++; // 如果字有重複，增加其次数
        } else {
          wordCounts[secondName] = 1; // 如果字沒重複，設次數為1
        }
      }
      for (let i = 0; i < data.length; i++) {
        let name = data[i];
        let secondName = name[1]; // 得到每個字串的第二個字
        if (wordCounts[secondName] === 1) {
          result.push(name);
        }
      }
      return result;
    }
  
      let nonRepSecNames = getSecondName(data);
  
      if(nonRepSecNames.length === 0){// 得到沒顯示名字的陣列
        console.log("沒有");
      }else{
        console.log(nonRepSecNames.toString());
      }
  }
  func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
  func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
  func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有


  console.log("== task4 ==")
  function getNumber(n) {
    let result = 0;
    for (let i = 1; i <= n; i++) {
      if (i % 2 === 1) {
        result += 4; // 奇數加4
      } else {
        result -= 1; // 偶數減1
      }
    }
    console.log(result);
  }
  
  getNumber(1); // print 4
  getNumber(5); // print 10
  getNumber(10); // print 15