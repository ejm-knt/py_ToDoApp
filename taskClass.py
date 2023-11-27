# タスククラスの定義
class Task:
    def __init__(self, content, date,):
        self.content = content  # タスクの内容
        self.date = date  # タスクの日付

    def __repr__(self):
        return f'Task(content={self.content}, date={self.date})'