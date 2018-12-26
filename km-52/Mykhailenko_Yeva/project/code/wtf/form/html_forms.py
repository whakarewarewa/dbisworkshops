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
                                             validators.Regexp('^[A-Z][a-z]+[\s]([A-Z][a-z]+)*$',
                                                               message='Invalid name')])
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
                                             validators.Regexp('^[A-Z][a-z]+[\s]([A-Z][a-z]+)*$',
                                                               message='Invalid name')])
    id = StringField('Contract ID: ', validators=[validators.DataRequired('Required'),
                                                  validators.Length(6, 6, "6 symbols allowed"),
                                                  validators.Regexp('^[0-9]', message='Only numeric')])

    submit = SubmitField('Sign up')


class FindDisciplineForm(FlaskForm):
    discipline = StringField('Enter discipline title in CAPS:',
                             validators=[validators.DataRequired(), validators.Length(1, 30),
                                         validators.Regexp('^[A-Z ]+$', message='Only big letters please')])
    submit = SubmitField('Find')


class EditPasswordForm(FlaskForm):
    password = PasswordField('', validators=[validators.DataRequired('Required'),
                                             validators.Length(1, 30, "Should be between 1 and 30")])
    submit = SubmitField('Update')


class DeleteUserForm(FlaskForm):
    delete = SubmitField('Delete profile')


class AddDisciplineForm(FlaskForm):
    dscpln_name = StringField('Discipline: ', validators=[validators.DataRequired('Required'),
                                                          validators.Length(1, 30, "Should be between 1 and 30"),
                                                          validators.Regexp('^[A-Z ]+$',
                                                                            message='Only big letters please')])

    submit = SubmitField('Add')


class HomeworkAddForm(FlaskForm):
    homework_date = StringField(validators=[validators.DataRequired('Required'),
                                            validators.Length(10, 10, "Should 10 symbols"),
                                            validators.Regexp('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))',
                                            message='Format YYYY-MM-DD please!')])
    description = StringField(validators=[validators.DataRequired('Required'), validators.Length(1, 300,
                              message='Over than 300 characters')])
    submit = SubmitField("Add")


class MarkAddForm(FlaskForm):
    student = StringField(validators=[validators.DataRequired('Required'),
                                      validators.Length(6, 6, "6 symbols allowed"),
                                      validators.Regexp('^[0-9]', message='Only numeric')])
    mark = IntegerField(validators=[validators.DataRequired('Required'), validators.NumberRange(0, 100,
                        message='Between 1 and 100')])
    st_year = IntegerField(validators=[validators.DataRequired('Require a number'), validators.NumberRange(1999, 2019,
                           message='Between 1999 and 2019')])
    submit = SubmitField("Add")
