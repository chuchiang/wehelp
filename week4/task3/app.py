from flask import Flask  # 載入Flask
from flask import request  # 載入 Request 物件
from flask import render_template  # 載入 render_template 涵式
from flask import redirect  # 載入redirect 涵式
from flask import url_for
from flask import session


# 建立 Application 物件，設定靜態檔案處理
app = Flask(__name__, static_folder="static", static_url_path="/")

app.secret_key="stringsecret" #設定session密碼




# 使用預設GET方法處理路徑/對應的涵式
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["post"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    session["account"]=account
    session["password"]=password
    if account == "test" and password == "test":
        session["SIGNED-IN"] = True
        return redirect( url_for ("member")) 
    elif account =="" or password =="": #都是字串類型
        return redirect( url_for ("error", message="請輸入帳號和密碼")) 
    else:
        # 驗證失敗，重新到向錯誤頁面，並錯誤訊息傳送到URL中。想要驗證失敗充新導向時，使用 redirect()
        return redirect( url_for ("error", message="帳號或密碼不正確"))

@app.route("/member")
def member():
    # 檢查 SIGNED-IN 狀態
    if not session.get("SIGNED-IN", False):
        return redirect(url_for("index"))
    return render_template("member.html")

@app.route("/signout")
def signout():
    session['SIGNED-IN'] = False  # 設定 SIGNED-IN 狀態為 FALSE
    return redirect(url_for("index"))

@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", message=message)


# 啟動伺服器在 Port 3000
app.run(port=3000)
