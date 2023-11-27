from datetime import datetime

# タスククラスの定義
class Task:
    """
    タスククラス

    引数:
    content (str): タスクの内容
    deadLineTaskDate (str): タスクの期日。形式は 'yyyy-mm-dd HH:MM'
    manegerName (str): タスクの担当者名
    """
    def __init__(self, content, deadLineTaskDate, manegerName):
        self.content = content                      # タスクの内容
        self.createTaskDate = datetime.now()        # タスク作成時刻
        self.deadLineTaskDate = datetime.strptime(deadLineTaskDate, '%Y-%m-%d') #タスク期日
        self.manegerName = manegerName              # タスク担当者

    def __repr__(self):
        return f'Task(content={self.content},CTDate={self.createTaskDate},DLTDate={self.deadLineTaskDate},manegerName={self.manegerName})'

    def remaining_days(self):
        delta = self.deadLineTaskDate - self.createTaskDate
        return delta.days

taskContents = Task("test", "2023-11-30", "江島")
print(taskContents)

days = taskContents.remaining_days()
print(days)

