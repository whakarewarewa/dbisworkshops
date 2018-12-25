import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json

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


@app.route('/select_reg')
def select_reg():
    return render_template('select_reg.html')


@app.route('/registration_student', methods=['GET', 'POST'])
def registration_student():
    form = RegisterSForm()
    if request.method == 'GET':
        login = request.cookies.get('cookie_name')
        if login is None:
            return render_template('registration_student.html', myform=form)
        return 'you already in'
    if request.method == 'POST':
        if not form.validate():
            return render_template('registration_student.html', myform=form)
        else:
            res = register_student(request.form['login'], request.form['id'])
            if res:
                return 'login or id is used'
            else:
                session['role'] = 'STUDENT'
                add_student(request.form['login'], request.form['password'], request.form['id'], request.form['name'],
                            request.form['st_semester'])
                response = make_response(redirect('/profile'))
                expires = datetime.now()
                expires += timedelta(days=60)
                response.set_cookie('cookie_name', request.form['login'], expires=expires)
                return response


@app.route('/registration_teacher', methods=['GET', 'POST'])
def registration_teacher():
    form = RegisterTForm()
    if request.method == 'GET':
        login = request.cookies.get('cookie_name')
        if login is None:
            return render_template('registration_teacher.html', myform=form)
        return 'you already in'
    if request.method == 'POST':
        if not form.validate():
            return render_template('registration_teacher.html', myform=form)
        else:
            res = register_teacher(request.form['login'], request.form['id'])
            if res:
                return 'login or id is used'
            else:
                session['role'] = 'TEACHER'
                add_teacher(request.form['login'], request.form['password'], request.form['id'], request.form['name'])
                response = make_response(redirect('/profile'))
                expires = datetime.now()
                expires += timedelta(days=60)
                response.set_cookie('cookie_name', request.form['login'], expires=expires)
            return response


@app.route('/disciplines', methods=['GET', 'POST'])
def disciplines():
    form = FindDisciplineForm()
    disc_table = list(all_discipline())

    if form.validate_on_submit():
        cursor = [item[0] for item in get_discipline(disc_name=request.form['discipline'])]
        return render_template('disciplines.html', form=form, cursor=cursor, disc_table=disc_table)

    return render_template('disciplines.html', form=form, disc_table=disc_table)


@app.route('/disciplines/<name>')
def named_discipline(name: str):
    marks = list(get_discipline_marks(disc_name=name))
    hw = list(get_discipline_hw(disc_name=name))

    return render_template('info_table.html', marks=marks, hw=hw, disc_name=name)


@app.route('/profile', methods=['GET','POST'])
def personal_profile():
    login = request.cookies.get('cookie_name')
    form = DeleteUserForm()
    myform = EditPasswordForm()
    if session['role'] == 'STUDENT':
        table1 = list(get_student_info(login=login))
        table2 = list(get_student_marks(login=login))
        if myform.validate_on_submit():
            upd_st_password(login=login, password=request.form['password'])
            response = make_response(redirect('/profile'))
            return response
    else:
        table1 = list(get_teacher_info(login=login))
        table2 = list(get_teacher_discipline(login=login))
        if myform.validate_on_submit():
            upd_t_password(login=login, password=request.form['password'])
            response = make_response(redirect('/profile'))
            return response
    return render_template('profile.html', login=login, table1=table1, table2=table2, form=form, myform=myform)


@app.route('/delete_profile', methods=['GET', 'POST'])
def delete_profile():
    login = request.cookies.get('cookie_name')
    if request.method == 'GET':
        if session['role'] == 'STUDENT':
            response = make_response(redirect('/'))
            response.set_cookie('cookie_name', '', 0)
            session['role'] = None
            delete_student(login)
            return response
        if session['role'] == 'TEACHER':
            response = make_response(redirect('/'))
            response.set_cookie('cookie_name', '', 0)
            session['role'] = None
            delete_teacher(login)
            return response


@app.route('/add_discipline', methods=['GET', 'POST'])
def add_discipline():
    form = AddDisciplineForm()
    if form.validate_on_submit():
        res = check_discipline(dscpln_name=request.form['dscpln_name'])
        if res:
            return render_template('add_discipline.html', myform=form)
        else:
            new_discipline(request.form['dscpln_name'])
            response = make_response(redirect('/disciplines'))
            return response
    return render_template('add_discipline.html', myform=form)


@app.route('/graph')
def visualize():
    graph = graph1()
    value = graph.discipline_count()
    print(value)
    disciplines=[]
    counts=[]
    for row in value:
        disciplines+=[row[0]]
        counts+=[row[1]]

    data = go.Bar(x=disciplines, y=counts)
    layout = go.Layout(title='Discipline average mark', xaxis=dict(title='Discipline name'),
                       yaxis=dict(title='Mark',  rangemode='nonnegative', autorange=True))
    data2 = [data]
    fig = go.Figure(data=data2, layout=layout)
    result = py.plot(fig)
    graphJson = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graphs.html', graphJson=graphJson)


if __name__ == "__main__":
    app.run()
