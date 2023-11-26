
#! classを作るときは__init__関数でコンストラクタを設定可能
class Task:
    def __init__(self, content, date):
        self.content = content  # タスクの内容
        self.date = date  # タスクの日付

#! __repr__ メソッドは、オブジェクトの「公式」文字列表現を返すためのものです。
#! これはオブジェクトを可能な限り完全に再現することを目指しています。
#! これをオンにすると、print関数で中身がきちんと表示される。(オフだとメモリ内容がそのまま出力)
    def __repr__(self):
        return f'Task(content={self.content}, date={self.date})'

pjList = {} #? ディクショナリ定義

#! tasks01 に格納するタスククラスを定義
content011 = "pj1"
date011 = "2023/11/25"

#! tasks01 を新しく定義、タスクリストにタスク01を格納
tasks01 = []
tasks01.append(Task(content011, date011))

#! pJDict にプロパティをつけてtasks01を格納
pjList["pj1"] = tasks01

#! tasks02 に格納するタスククラスを複数定義
content021 = "pj2-1"
date021 = "2023/11/26"
content022 = "pj2-2"
date022 = "2023/11/27"

#! tasks02 を pjDict に格納
tasks02 = []
tasks02.append(Task(content021, date021))
tasks02.append(Task(content022, date022))
pjList["pj2"] = tasks02

#! それぞれを表示
print(tasks01)
print(tasks02)
print(pjList)
