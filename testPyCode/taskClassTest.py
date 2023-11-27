from datetime import datetime

# タスククラスの定義
class Task:
    """
    TaskClass_引数:
    content (str): タスクの内容
    deadLineTaskDate (str): タスクの期日。形式は 'yyyy-mm-dd HH:MM'
    manegerName (str): タスクの担当者名
    """
    def __init__(self, content, deadLineTaskDate, manegerName, taskStatus="ToDo"):
        self.content = content                      # タスクの内容
        self.createTaskDate = datetime.now()        # タスク作成時刻
        self.deadLineTaskDate = datetime.strptime(deadLineTaskDate, '%Y-%m-%d') #タスク期日
        self.manegerName = manegerName              # タスク担当者
        self.taskStatus = taskStatus                # タスクの進捗状態
        self.taskComment = []                       # タスクに対するコメント

    def __repr__(self):
        return f'Task(content={self.content},CTDate={self.createTaskDate},DLTDate={self.deadLineTaskDate},manegerName={self.manegerName})'

    def remaining_days(self):
        """期日 -  作成日"""
        delta = self.deadLineTaskDate - self.createTaskDate
        return delta.days

    def statusChange(self, taskStatus):
        """Choose from the following items\n
        "ToDo":"未着手"\n
        "Doing":"進行中"\n
        "Done":"完了"\n
        "Pending":"保留"\n
        "Cancel":"中止"
        """
        self.taskStatus = taskStatus