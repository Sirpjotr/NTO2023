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


@app.route("/users")
def users():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    print(users)
    #return 'OK'
    #users = db.session.query().all()
    return render_template("users.html", users=users)


@app.route("/create-user", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return "Аккаунт с такой почтой уже зарегистрирован"

    else:
        return render_template("create-user.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
