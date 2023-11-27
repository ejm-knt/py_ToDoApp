class Task:
    def __init__(self, content, date):
        self.content = content  # タスクの内容
        self.date = date  # タスクの日付

    def __repr__(self):
        return f'Task(content={self.content}, date={self.date})'

class ProjectManager:
    def __init__(self):
        self.projects = {}  # 各プロジェクトを格納するディクショナリ

    # プロジェクトを追加する
    def add_project(self, name):
        if not (name in self.projects) :
            self.projects[name] = []
        else:
            print(f"プロジェクト {name} は既に存在しています。")

    # プロジェクトを削除する
    def remove_project(self, project_name):
        if project_name in self.projects:
            del self.projects[project_name]
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # タスクを追加する
    def add_task(self, project_name, task):
        if project_name in self.projects:
            self.projects[project_name].append(task)
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # タスクを削除する
    def remove_task(self, project_name, index):
        if project_name in self.projects:
            try:
                self.projects[project_name].pop(index)
            except IndexError:
                print(f"プロジェクト {project_name} にはインデックス {index} のタスクは存在しません。")
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # プロジェクトとそのタスクを表示する
    def display_projects(self):
        for project, tasks in self.projects.items():
            print(f"{project}: {tasks}")

# プロジェクトマネージャーを作成
pm = ProjectManager()

# プロジェクトとタスクを追加

while True:
    selectMode = int(input("0:DictView 1:pjAdd 2:pjDel 3:taskAdd 4:taskDel 5:end >> "))

    if selectMode == 0:
        pm.display_projects()

    elif selectMode == 1:
        # pm.add_project("pj1")
        pm.add_project(input("addするpj名を入力 >> "))

    elif selectMode == 2:
        pm.remove_project(input("removeするpj名を入力 >> "))

    elif selectMode == 3:
        pjName = input("追加したいpj名を入力 >> ")
        addContent = input("追加したいtask内容を入力 >> ")
        addDate = input("追加したtimeを入力 >> ")
        task = Task(addContent,addDate)
        pm.add_task(pjName, task)

    elif selectMode == 4:
        pjName = input("削除したいpj名を入力 >> ")
        for tList in pm.projects[pjName]:
            print(tList)
        delTaskIndex = int(input("削除したtask番号を入力 >> "))
        pm.remove_task(pjName, delTaskIndex)

    elif selectMode == 5:
        break

    pm.display_projects()