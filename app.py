from venv import create

from flask import Flask, render_template
from routes.useer_routes import user_routes
from models.users import create_user_table, seed_users
app = Flask(__name__)
app.register_blueprint(user_routes)
def initialize_db():
    create_user_table()
    seed_users()
@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    initialize_db()
    app.run(host='0.0.0.0', port=5000,debug=True)
