from flask import Flask, render_template, request, redirect, url_for
from models import User, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345678@localhost:5432/history"
db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/study_page')
def study_page():
    return render_template('study_page.html')


@app.route('/price')
def price():
    return render_template('price.html')


@app.route('/sign', methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        email = request.form['email']
        password1 = request.form['password']
        password2 = request.form['repeat_password']
        if str(password2) != str(password1):
            return redirect(url_for('sign'))
        else:
            response = User(email = email, password = password1)
            db.session.add(response)
            db.session.commit()
            return render_template('login.html')
    else:
        return render_template('signin.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect('index.html')
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
