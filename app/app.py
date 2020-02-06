# flaskとrender_template(HRMLを表示させるための関数)をインポート
from flask import Flask, render_template, request

# flaskオブジェクトの生成

app = Flask(__name__)

# ルーティング。/にアクセスされたらhelloメソッドを実行する
@app.route("/")
# ルーティング。/indexへアクセスされたらindexメソッドを実行する
@app.route("/index")
def index():
    name = request.args.get("name")  # request.args.getでクエリストリングを受け取ることができる

    # render_templateの引数に入れることでhtml側に送ることができる
    return render_template("index.html", name=name)


@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
