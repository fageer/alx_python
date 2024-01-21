from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'
###############################################################

db = SQLAlchemy(app)

############################  TO DO 2 ##############################

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)


def create_tables():
    with app.app_context():
        db.create_all()

create_tables()


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!')
    return render_template('add_user.html')


@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        user = User.query.get(user_id)
        user.name = name
        user.email = email
        db.session.commit()
        flash('User updated successfully!')
    return render_template('update_user.html', user=user)


@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!')
    return render_template('delete_user.html', user=user)
#################################################################


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    