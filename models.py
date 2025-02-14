from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Todo(db.Model):
    todo_id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200))
    completed=db.Column(db.Boolean,default=False)
    user_id=db.Column(db.Integer)
    clear=db.Column(db.Boolean,default=False)
    priority =db.Column(db.String(20))
    deadline=db.Column(db.Date)
    completed_date=db.Column(db.String(20))
    file_url = db.Column(db.String(200)) 
    
    def __repr__(self):
        return f"<Todo {self.title}>"
    
class User(db.Model):
    user_id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(20))
    lname=db.Column(db.String(20))
    email = db.Column(db.String(120),unique=True)
    phone=db.Column(db.String(10))
    password= db.Column(db.String(20))
    