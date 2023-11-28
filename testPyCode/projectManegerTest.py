from taskClassTest import Task

class ProjectManager:
    def __init__(self):
        self.projects = {}  # 各プロジェクトを格納するディクショナリ

    # プロジェクトを追加する
    def addProject(self, name):
        if not (name in self.projects) :
            self.projects[name] = []
        else:
            print(f"プロジェクト {name} は既に存在しています。")

    # プロジェクトを削除する
    def removeRroject(self, project_name):
        if project_name in self.projects:
            del self.projects[project_name]
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # タスクを追加する
    def addTask(self, project_name, task):
        if project_name in self.projects:
            self.projects[project_name].append(task)
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # タスクを削除する
    def removeTask(self, project_name, index):
        if project_name in self.projects:
            try:
                self.projects[project_name].pop(index)
            except IndexError:
                print(f"プロジェクト {project_name} にはインデックス {index} のタスクは存在しません。")
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # プロジェクトとそのタスクを表示する
    def displayProjects(self):
        for project, tasks in self.projects.items():
            print(f"{project}: {tasks}")

pm = ProjectManager()
while True:
    selectMode = int(input("0:DictView 1:pjAdd 2:pjDel 3:taskAdd 4:taskDel 5:end >> "))

    if selectMode == 0:
        pm.displayProjects()

    elif selectMode == 1:
        # pm.add_project("pj1")
        pm.addProject(input("addするpj名を入力 >> "))

    elif selectMode == 2:
        pm.removeRroject(input("removeするpj名を入力 >> "))

    elif selectMode == 3:
        pjName = input("追加したいpj名を入力 >> ")
        addContent = input("追加したいtask内容を入力 >> ")
        addDate = input("期日を入力(YYYY-MM-DD形式) >> ")
        addManeger = input("担当者を入力 >>")
        task = Task(addContent,addDate,addManeger)
        pm.addTask(pjName, task)

    elif selectMode == 4:
        pjName = input("削除したいpj名を入力 >> ")
        for tList in pm.projects[pjName]:
            print(tList)
        delTaskIndex = int(input("削除したtask番号を入力 >> "))
        pm.removeTask(pjName, delTaskIndex)

    elif selectMode == 5:
        break

    pm.displayProjects()