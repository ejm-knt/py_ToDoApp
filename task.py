# Flaskとその他の必要なライブラリをインポート
from flask import Flask, render_template, request, session

from taskClass import Task
from taskManegerClass import ProjectManager

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # セッションを安全に使用するための秘密鍵

# プロジェクトマネージャーclassの取得/定義
pjm = ProjectManager()

# ルートURLへのアクセスを処理
@app.route('/', methods=['GET', 'POST'])
def index():
    # POSTリクエストの場合
    if request.method == 'POST':

        # pjAddが送信された場合
        if request.form.get('pjAdd'):
            request.form.get('pjAdd') == 'createPJ'
            pjm.add_project(request.form.get('newPjName'))

        # 'Remove'ボタンが押され、かつカウントが0より大きい場合
        if request.form.get('remove') == 'pjRemove':
            removed_value = d.pop('k1')
            print(d)
            # {'k2': 2, 'k3': 3}

        # tasksAddが送信された場合
        if request.form.get('newPjName'):
            content = request.form.get('newPjName')  # タスクの内容を取得
            tasks.append(Task(content, date))  # タスクをリストに追加


    # index.htmlをレンダリングしてレスポンスを返す
    return render_template('index.html', pjmDict = pjm.projects, count=session['count'])

# スクリプトが直接実行された場合にサーバーを起動
if __name__ == '__main__':
    app.run(debug=True)  # デバッグモードでサーバーを起動
