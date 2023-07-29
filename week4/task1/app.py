from flask import Flask  # 載入Flask
from flask import request  # 載入 Request 物件
from flask import render_template  # 載入 render_template 涵式
# 建立 Application 物件，設定靜態檔案處理
app = Flask(__name__, static_folder="static", static_url_path="/")

# 使用預設GET方法處理路徑/對應的涵式


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["post"])
def signin():
    return render_template("signin.html")



# 啟動伺服器在 Port 3000
app.run(port=3000)
