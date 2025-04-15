from src.models.user import User
from src import db

def add_user(name):
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return new_user 

def get_all_users():
    users = User.query.all()  
    return users

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

