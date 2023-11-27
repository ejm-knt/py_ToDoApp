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

    # # タスクを削除する
    # def remove_task(self, project_name, task, index):
    #     if project_name in self.projects and :
            
    #     else:
    #         print(f"プロジェクト {project_name} は存在しません。")

    # プロジェクトとそのタスクを表示する
    def display_projects(self):
        for project, tasks in self.projects.items():
            print(f"{project}: {tasks}")

# プロジェクトマネージャーを作成
pm = ProjectManager()

# プロジェクトとタスクを追加

# while True:
#     input("1:pjAdd 2:pjDel 3:taskAdd 4:taskDel")
pm.add_project("pj1")
pm.add_task("pj1", Task("task1", "2023-11-26"))

pm.add_project("pj2")
pm.add_task("pj2", Task("task1", "2023-11-27"))
pm.add_task("pj2", Task("task2", "2023-11-28"))

# 結果を表示
pm.display_projects()

print(pm.projects["pj1"])