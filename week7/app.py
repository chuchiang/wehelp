from flask import Flask  # 載入Flask
from flask import jsonify # 處理返回序列化的json數據
import json
from flask import request  # 載入 Request 物件
from flask import render_template  # 載入 render_template 涵式
from flask import redirect  # 載入redirect 涵式
from flask import url_for
from flask import session
import mysql.connector


# 建立 Application 物件，設定靜態檔案處理
app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key="stringsecret" #設定session密碼

#創建連線
db = mysql.connector.connect(
    host="localhost", #mysql 位置 
    port="3306",  #連接通道
    user="root",
    password="2926",
    database="website" #直接使用這個資料庫
)

cursor=db.cursor(dictionary=True)

# 使用預設GET方法處理路徑/對應的涵式
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/member")
def api():
    username = request.args.get("username")#request.args.get [get請求]，request.form[post請求]
    query = "SELECT id, name, username FROM member WHERE username = %s "
    values=(username,)
    cursor.execute(query,values)
    member_data = cursor.fetchone()# 只獲取一個成員的信息
    if member_data:
        data=jsonify({"data": member_data})
        return data
    else:   
        return jsonify({"data": None})# 返回会员数据的JSON响应
    

def replacename_taken(sql_name,sql_username):
    query = "UPDATE member SET NAME= %s WHERE username = %s"
    values = (sql_name,sql_username)
    cursor.execute(query, values)
    result = cursor.fetchall()
    return result is not None


@app.route("/api/member",methods=["PATCH"])
def apiname():
    # 解析前端傳來的 JSON 數據
    data = request.json
    new_name = data.get("name")
    session["name"] = new_name
    sql_name=session.get("name","")
    sql_username=session.get("account","")

    # 根據需要在數據庫中更新成員的用戶名
    # 假設更新成功後，你可以返回一個 JSON 響應來表示更新成功
    if replacename_taken(sql_name,sql_username): 
        sql_ok=jsonify({"ok": "true"})
        return sql_ok
    else:
        return jsonify({"error": "true"})
    

def username_taken(signup_account):
    query = "SELECT * FROM member WHERE username = %s"
    values = (signup_account,)#如果不加,會被賦值為 username 的值，而不是一個包含 username 的元組，在執行資料庫查詢時，我們通常使用元組來傳遞參數
    cursor.execute(query, values)
    result = cursor.fetchone()
    return result is not None

def register_taken(signup_name, signup_account, signup_password):
    query = "INSERT INTO member(name,username,password) VALUES ( %s, %s, %s)"
    values = (signup_name, signup_account, signup_password)
    cursor.execute(query, values)
    db.commit()

@app.route("/signup", methods=["post"])
def signup():
    signup_name = request.form["signup_name"]
    signup_account = request.form["signup_account"]
    signup_password = request.form["signup_password"]

    if username_taken(signup_account)==True:
        return redirect( url_for ("error", message="帳號已經被註冊")) 
    else:
        register_taken(signup_name, signup_account, signup_password)
        return redirect(url_for("index")) 


def signin_taken(account,password):
    query = "SELECT * FROM member WHERE username= %s and  password=%s"
    values = (account,password)
    cursor.execute(query, values)
    result = cursor.fetchone()
    return result is None

def name_taken(account,password):
    query = "SELECT name FROM member WHERE username=%s and  password=%s"
    values = (account,password)
    cursor.execute(query, values)
    sql_name = cursor.fetchone()
    return sql_name["name"]

def id_taken(account,password):
    query = "SELECT id FROM member WHERE username=%s and  password=%s"
    values = (account,password)
    cursor.execute(query, values)
    sql_id = cursor.fetchone()
    return sql_id["id"]


@app.route("/signin", methods=["post"])
def signin():
    account = request.form["account"]
    password = request.form["password"]

    if signin_taken(account,password)==True:
        return redirect( url_for ("error", message="帳號或密碼輸入錯誤"))
    else:
        name=name_taken(account,password)
        id=id_taken(account,password)
        session["account"]=account
        session["password"]=password
        session["id"]=id
        session["name"]=name
        session["SIGNED-IN"] = True
        return redirect( url_for ("member"))

@app.route("/member")
def member():
    # 檢查 SIGNED-IN 狀態
    cursor.execute("SELECT member.name,message.content,message.id FROM member INNER JOIN message on member.id=message.member_id ORDER BY message.id;")
    sql_content = cursor.fetchall()
    name = session.get("name", "") # 從session取得name
    return render_template("member.html",sql_content=sql_content,name=name)

    
@app.route("/createMessage", methods=["post"])
def content():
    comment=request.form["comment"]
    id=session["id"]
    query=("INSERT INTO message (member_id,content) VALUES(%s,%s);")
    values=(id,comment)
    cursor.execute(query,values)
    db.commit()
    return redirect(url_for("member"))



@app.route("/deleteMessage",methods=["post"])
def deleteMessage():
    data = request.data.decode("utf-8")  # 解碼接收的純文本數據
    query = "DELETE FROM message WHERE id=%s"
    values = (data,)  #  將數字包裝成 tuple(MySQL Connector 要求參數應該是 list、tuple 或 dict 類型)
    cursor.execute(query, values)
    db.commit()
    return redirect(url_for("member"))



@app.route("/signout")
def signout():
    session['SIGNED-IN'] = False  # 設定 SIGNED-IN 狀態為 FALSE
    del session['account']
    del session['password']
    del session['id']
    del session['name']
    return redirect(url_for("index"))

@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", message=message)


# 啟動伺服器在 Port 3000
app.run(port=3000)

cursor.close()#cursor 關閉
db.close()#連線 關閉
