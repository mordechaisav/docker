from flask import Blueprint, render_template, request, redirect, url_for
from models.users import get_all_users, add_user, delete_user

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users')
def users():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_routes.route('/add_user', methods=['POST'])
def add_user_route():
    name = request.form['name']
    email = request.form['email']
    add_user(name, email)
    return redirect(url_for('user_routes.users'))

@user_routes.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user_route(user_id):
    delete_user(user_id)
    return redirect(url_for('user_routes.users'))