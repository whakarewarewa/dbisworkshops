from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, IntegerField


class LoginForm(FlaskForm):
    login = StringField('Login: ', validators=[validators.DataRequired('Required')])
    password = PasswordField('Password: ', validators=[validators.DataRequired('Required')])

    submit = SubmitField('Sign in')


class RegisterSForm(FlaskForm):
    login = StringField('Login: ', validators=[validators.DataRequired('Required'),
                                               validators.Length(1, 20, "Login should be from 1 to 20 symbols"),
                                               validators.Regexp('^\S+$', message='No spaces please')])
    password = PasswordField('Password: ', validators=[validators.DataRequired('Required'),
                                                       validators.Length
                                                       (1, 30, "Password should be from 1 to 30 symbols")])
    name = StringField('Name: ', validators=[validators.DataRequired('Required'),
                                             validators.Length(1, 30, "Name should be from 1 to 30 symbols"),
                                             validators.Regexp('^[a-zA-Z ]+$', message='Only letters please')])
    id = StringField('Card ID: ', validators=[validators.DataRequired('Required'),
                                              validators.Length(6, 6, "6 symbols allowed"),
                                              validators.Regexp('^[0-9]', message='Only numeric')])
    st_semester = IntegerField('Study Semester: ', validators=[validators.DataRequired('Require a number'),
                                                               validators.NumberRange(min=1, max=10,
                                                                                      message='From 1 to 10')])
    submit = SubmitField('Sign up')


class RegisterTForm(FlaskForm):
    login = StringField('Login: ', validators=[validators.DataRequired('Required'),
                                               validators.Length(1, 20, "Login should be from 1 to 20 symbols"),
                                               validators.Regexp('^\S+$', message='No spaces please')])
    password = PasswordField('Password: ', validators=[validators.DataRequired('Required'),
                                                       validators.Length
                                                       (1, 30, "Password should be from 1 to 30 symbols")])
    name = StringField('Name: ', validators=[validators.DataRequired('Required'),
                                             validators.Length(1, 30, "Name should be from 1 to 30 symbols"),
                                             validators.Regexp('^[a-zA-Z ]+$', message='Only letters please')])
    id = StringField('Contract ID: ', validators=[validators.DataRequired('Required'),
                                                  validators.Length(6, 6, "6 symbols allowed"),
                                                  validators.Regexp('^[0-9]', message='Only numeric')])

    submit = SubmitField('Sign up')

