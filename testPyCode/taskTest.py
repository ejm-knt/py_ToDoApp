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
    if 'pjAddButton' in request.form:
        return projectAdd()
    elif 'pjRemoveButton' in request.form:
        return projectRemove()
    elif 'taskAddButton' in request.form:
        return taskAdd()
    elif 'taskRemoveButton' in request.form:
        return taskRemove()
    else:
        return render_template('index.html', pjmDict = pjm.projects)

def projectAdd():
    # プロジェクト追加の処理
    ...

def projectRemove():
    # プロジェクト削除の処理
    ...

def taskAdd():
    # タスク追加の処理
    ...

def taskRemove():
    # タスク削除の処理
    ...

    # index.htmlをレンダリングしてレスポンスを返す
    return render_template('index.html', pjmDict = pjm.projects)

# スクリプトが直接実行された場合にサーバーを起動
if __name__ == '__main__':
    app.run(debug=True)  # デバッグモードでサーバーを起動
