from flask import Flask, render_template, request, url_for, flash, redirect
from form import RegistrationForm, LoginForm
import os
app = Flask(__name__)


app.secret_key = os.urandom(24)


posts = [
    {
        'moive': 'u and me',
        'time': '2:00 pm'
    },
    {
        'moive': 'u and me 1',
        'time': '3:00 pm'
    },
    {
        'moive': 'u and me 2',
        'time': '4:00 pm'
    },
    {
        'moive': 'u and me 3',
        'time': '5:00 pm'
    },
]

app.config.from_object(__name__)

# this refresh auto
# app.debug = True


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/article')
def article():
    return render_template('article.html', posts=posts)


# testing form
@app.route('/student')
def student():
   return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html", result=result)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Create Success for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == '1234':
            flash('Login Success', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid Email or Password. Please check again','danger')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    # or can put here as in app.run(debig=true)
