from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dif-game")
def dg():
    return render_template("game.html")


@app.route("/simple-game")
def sg():
    return render_template("simple-game.html")


@app.route("/position")
def p():
    return render_template("position.html")


@app.route("/rotation")
def r():
    return render_template("twelve.html")


@app.route("/shadow")
def s():
    return render_template("tenth-task.html")


@app.route("/shadow-animation")
def sa():
    return render_template("ninth.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
