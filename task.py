# Flaskとその他の必要なライブラリをインポート
from flask import Flask, render_template, request, session
from datetime import datetime

# タスククラスの定義
class Task:
    def __init__(self, content, date, isView=True):
        self.content = content  # タスクの内容
        self.date = date  # タスクの日付
        self.isView = isView  # タスクの表示状態

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # セッションを安全に使用するための秘密鍵

# タスクリストの初期化
pjDict = {}
tasks = []

# ルートURLへのアクセスを処理
@app.route('/', methods=['GET', 'POST'])
def index():
    # セッションにカウントが存在しない場合は初期化
    if 'count' not in session:
        session['count'] = 0

    # POSTリクエストの場合
    if request.method == 'POST':

        # タスクが送信された場合
        if request.form.get('task'):
            content = request.form.get('task')  # タスクの内容を取得
            date = datetime.now().strftime('%Y-%m-%d %H:%M')  # 現在の日時を取得
            tasks.append(Task(content, date))  # タスクをリストに追加

        # 'Add'ボタンが押された場合
        elif request.form.get('add') == 'pjAdd':
            session['count'] += 1  # カウントを増やす
            

        # 'Remove'ボタンが押され、かつカウントが0より大きい場合
        elif request.form.get('remove') == 'pjRemove' and session['count'] > 0:
            session['count'] -= 1  # カウントを減らす

    # index.htmlをレンダリングしてレスポンスを返す
    return render_template('index.html', tasks=tasks, pjDict=pjDict, count=session['count'])

# スクリプトが直接実行された場合にサーバーを起動
if __name__ == '__main__':
    app.run(debug=True)  # デバッグモードでサーバーを起動
