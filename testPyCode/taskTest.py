# Flaskとその他の必要なライブラリをインポート
from flask import Flask, render_template, request
from taskClassTest import Task
from projectManegerTest import ProjectManager

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
        return render_template('formTest.html', pjmDict = pjm.projects.items())

def projectAdd():
    pjAddName = request.form.get('pjAdd')
    print(pjAddName)
    pjm.addProject(pjAddName)
    return render_template('formTest.html', pjmDict = pjm.projects.items())


def projectRemove():
    pjRemoveName = request.form.get('pjRemove')
    pjm.removeRroject(pjRemoveName)
    return render_template('formTest.html', pjmDict = pjm.projects.items())


def taskAdd():
    contents = request.form.get('contents')
    deadline = request.form.get('deadline')
    maneger  = request.form.get('maneger')
    pjName = request.form.get('test')
    pjm.addTask(pjName,Task(contents,deadline,maneger))
    return render_template('formTest.html', pjmDict = pjm.projects.items())


def taskRemove():
    pjName = request.form.get('test')
    removeTaskNum = request.form.get('taskListNum')
    pjm.removeTask(pjName,removeTaskNum)
    return render_template('formTest.html', pjmDict = pjm.projects.items())


    # # index.htmlをレンダリングしてレスポンスを返す
    # return render_template('index.html', pjmDict = pjm.projects)

# スクリプトが直接実行された場合にサーバーを起動
if __name__ == '__main__':
    app.run(debug=True)  # デバッグモードでサーバーを起動