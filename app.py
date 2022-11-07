from flask import Flask, render_template, request, redirect, url_for, session
from models import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345678@localhost:5432/history"
app.config['SECRET_KEY'] = 'superpupersecretkey'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():  # put application's code here
    if 'email' in session and 'password' in session:
        logout()
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
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        country = request.form['country']
        date_of_birth = request.form['date_of_birth']
        password1 = request.form['password']
        password2 = request.form['repeat_password']
        if str(password2) != str(password1):
            return redirect(url_for('sign'))
        else:
            response = User(email=email, password=password1,
                            first_name=first_name, second_name=second_name,
                            country=country, date_of_birth=date_of_birth)
            db.session.add(response)
            db.session.commit()
            return render_template('login.html')
    else:
        return render_template('signin.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        check = User.query.filter_by(email=email, password=password).all()
        # Если такого пользователя нет
        if check is None:
            return redirect(url_for('login'))
        else:
            # хранить пользователя
            session['email'] = email
            session['password'] = password
            return redirect(url_for('profile'))
    else:
        return render_template('login.html')


@app.route('/profile', methods=["GET", "POST"])
def profile():
    infos = User.query.filter_by(email=session['email'], password=session['password']).all()
    return render_template('profile.html', infos=infos)


@app.route('/logout')
def logout():
    #Очистить токены
    session.pop('email', None)
    session.pop('password', None)
    return render_template('index.html') 


if __name__ == '__main__':
    app.run()
