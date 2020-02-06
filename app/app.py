# flaskとrender_template(HRMLを表示させるための関数)をインポート
from flask import Flask,render_template

#flaskオブジェクトの生成

app = Flask(__name__)

#ルーティング。/にアクセスされたらhelloメソッドを実行する
@app.route("/")
def hello():
    return "Hello〜〜〜"

#ルーティング。/indexへアクセスされたらindexメソッドを実行する
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)