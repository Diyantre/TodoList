from flask import Flask, render_template, request, redirect, url_for
from model import todolist, create_table, delete_all, insert_todos, compter_taches
import datetime


app = Flask(__name__)


create_table()

delete_all()

if compter_taches() == 0:
    insert_todos("Ajouter une tache", "Cliquez sur submit")


@app.route('/', methods=["POST", "GET"])
def display_todo():
    todos = todolist.affiche_todos()
    return render_template('index.html', todos=todos)

@app.route('/savetodos', methods=["POST"])
def save_todos():
    newtache = request.form['add']
    newdesc = request.form['desc']
    insert_todos(newtache, newdesc)
    return redirect(url_for('display_todo'))

@app.route('/delete_todos', methods=["POST", "GET"])
def delete_todos():
    todo_id = request.args.get('id')
    todolist.delete_todos(todo_id)
    return redirect(url_for('display_todo'))

if __name__ == '__main__':
    app.run(debug=True)

