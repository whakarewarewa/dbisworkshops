from flask import Flask, render_template, request, make_response, redirect, session
from wtf.form.html_forms import *
from datetime import datetime, timedelta
from func import *
from vizualization import graph1

app = Flask(__name__)
app.secret_key = 'My_key'
plotly.tools.set_credentials_file(username='whakarewarewa', api_key='4f4aZHi2NsoUo5IIHYpp')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        log_in = request.cookies.get('cookie_name')
        return render_template('authorize.html', log_in=log_in)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        login = request.cookies.get('cookie_name')
        if login is None:
            return render_template('login.html', myform=form)
        return 'you already in'
    if request.method == 'POST':
        if not form.validate():
            return render_template('login.html', myform=form)
        else:
            check = check_user(request.form['login'])
            if check == 0:
                return 'No such login. Register first'
            else:
                res = login_user(request.form['login'], request.form['password'])
                session['role'] = get_role(username=request.form['login'])
                if res:
                    response = make_response(redirect('/'))
                    expires = datetime.now()
                    expires += timedelta(days=60)
                    response.set_cookie('cookie_name', request.form['login'], expires=expires)
                    return response
                else:
                    return 'Wrong password'


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global response
    if request.method == 'GET':
        response = make_response(redirect('/'))
        response.set_cookie('cookie_name', '', 0)
        session['role'] = None
    return response


if __name__ == "__main__":
    app.run()
