import sqlite3
import datetime


def delete_all():
    db = sqlite3.connect("taches.db")
    c = db.cursor()
    c.execute('''
              DELETE FROM taches
              ''') 

    db.commit()
    c.execute('''DELETE FROM sqlite_sequence WHERE name='taches';''')
    db.commit()
    db.close()
    
    
def create_table():
    db = sqlite3.connect("taches.db")
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS taches
              (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  todos TEXT NOT NULL,
                  description TEXT NOT NULL,
                  heure DATE NOT NULL
              )
              ''') 
    db.commit()
    db.close()
    

def insert_todos(taches, desc):
        db = sqlite3.connect("taches.db")
        c = db.cursor()
        c.execute('''
                   INSERT INTO taches(todos, description, heure) VALUES
                   (?,?,?)
                   ''', (taches, desc, datetime.datetime.now())
                   )
        db.commit()
        db.close()


def compter_taches():
    with sqlite3.connect("taches.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM taches")
        return cursor.fetchone()[0]

class todolist():
    
    def __init__(self, taches, desc, date):
        self.taches = taches
        self.desc = desc
        self.date = date
        
    def get_taches(self):
        return self.taches

    def get_desc(self):
        return self.desc

    def get_date(self):
        return self.date

   
    
    def delete_todos(id):
        db = sqlite3.connect("taches.db")
        c = db.cursor()
        c.execute('''
                  DELETE FROM taches WHERE id = ?
                  ''', (id)
                  )
        db.commit()
        db.close()
    
    
    def affiche_todos():
        db = sqlite3.connect("taches.db")
        c = db.cursor()
        c.execute("SELECT id, todos, description FROM taches")
        todos = c.fetchall()
        db.close()
        return todos
        
    def update_todos(taches, newtache):
        db = sqlite3.connect("taches.db")
        c = db.cursor()
        c.execute('''
                  UPDATE taches SET ? = ?
                  WHERE ? = ?
                  ''', (taches, newtache,taches, taches)
                  )
        db.commit()
        db.close()
    