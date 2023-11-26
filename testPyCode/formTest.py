from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # セッションを安全に使用するための秘密鍵

tasks = []
pjList = []

@app.route('/formTest', methods=['GET', 'POST'])
def formTest():
    # セッションにカウントが存在しない場合は初期化
    if 'count' not in session:
        session['count'] = 0
        
    # POSTリクエストの場合
    if request.method == 'POST':
        content = request.form.get("textTest")
        tasks.append(content)

    # index.htmlをレンダリングしてレスポンスを返す
    return render_template('formTest.html', test = tasks, pjList = pjList, count=session['count'])

# スクリプトが直接実行された場合にサーバーを起動
if __name__ == '__main__':
    app.run(debug=True)  # デバッグモードでサーバーを起動
