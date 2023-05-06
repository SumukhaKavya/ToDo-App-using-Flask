from flask import Flask,render_template,request,redirect,url_for
app=Flask('ToDo App')
tasks=[]
@app.route('/')
def home():
    return render_template('index.html',tasks=tasks)
@app.route('/add',methods=['POST'])
def add():
    task_description=request.form['task']
    tasks.append(task_description)
    return redirect(url_for('home'))
