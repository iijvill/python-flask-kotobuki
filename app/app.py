# flaskとrender_template(HRMLを表示させるための関数)をインポート
from flask import Flask, render_template, request

app = Flask(__name__)  # flaskオブジェクトの生成

# ルーティング。/indexへアクセスされたらindexメソッドを実行する
@app.route("/index")
def index():

    # render_templateの引数に入れることでhtml側に送ることができる
    return render_template("index.html")


@app.route("/result", methods=["post"])
def post():
    input_str = request.form['target_str']

    table = str.maketrans({
        'i': 'l',
        'I': 'L',
        'l': 'i',
        'L': 'I',
        'c': 'エ',
        'C': 'エ',
        'n': 'ホ',
        'N': 'ホ',
        'o': 'Γ',
        'O': 'Γ',
    })

    translate_str = input_str.translate(table)

    return render_template("index.html", ijitsu=translate_str)


if __name__ == "__main__":
    app.run(debug=True)
