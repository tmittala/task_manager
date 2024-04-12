from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tushar'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


db = SQLAlchemy()
db.init_app(app)

from routes import *

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()  # This line creates the database with all the tables
    app.run(debug=False)
