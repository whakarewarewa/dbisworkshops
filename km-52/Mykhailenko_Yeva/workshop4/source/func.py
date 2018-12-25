import cx_Oracle


user_login = 'eve'
password = 'eve'
server = 'xe'

conn = cx_Oracle.connect(user_login, password, server)
cursor = conn.cursor()


def login_user(login, password):
    return cursor.callfunc('user_package.login_user', cx_Oracle.NUMBER, [login, password])


def check_user(login):
    return cursor.callfunc('user_package.check_user', cx_Oracle.NUMBER, [login])


def check_discipline(dscpln_name):
    return cursor.callfunc('discipline_package.check_discipline', cx_Oracle.NUMBER, [dscpln_name])


def get_role(username):
    return cursor.callfunc('user_package.get_role', cx_Oracle.STRING, [username])


def register_student(login, id):
    return cursor.callfunc('user_package.register_student', cx_Oracle.NUMBER, [login, id])


def register_teacher(login, id):
    return cursor.callfunc('user_package.register_teacher', cx_Oracle.NUMBER, [login, id])


def add_teacher(login, password, id, name):
    return cursor.callproc('teacher_package.add_teacher', [login, password, id, name])


def add_student(login, password, id, name, st_semester):
    return cursor.callproc('student_package.add_student', [login, password, id, name, st_semester])

