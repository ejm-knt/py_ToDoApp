from flask import Flask, render_template, request, session
from datetime import datetime

class Task:
    def __init__(self, content, date, isView=True):
        self.content = content
        self.date = date
        self.isView = isView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'count' not in session:
        session['count'] = 0

    if request.method == 'POST':
        if request.form.get('task'):
            content = request.form.get('task')
            date = datetime.now().strftime('%Y-%m-%d %H:%M')
            tasks.append(Task(content, date))
        elif request.form.get('add') == 'Add':
            session['count'] += 1
        elif request.form.get('remove') == 'Remove' and session['count'] > 0:
            session['count'] -= 1

    return render_template('index.html', tasks=tasks, count=session['count'])

if __name__ == '__main__':
    app.run(debug=True)