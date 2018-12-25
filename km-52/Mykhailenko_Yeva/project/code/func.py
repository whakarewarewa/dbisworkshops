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


def get_student_info(login):
    return cursor.callfunc('student_package.get_student_info', cx_Oracle.CURSOR, [login])


def get_student_marks(login):
    return cursor.callfunc('student_package.get_student_marks', cx_Oracle.CURSOR, [login])


def get_teacher_info(login):
    return cursor.callfunc('teacher_package.get_teacher_info', cx_Oracle.CURSOR, [login])


def get_teacher_discipline(login):
    return cursor.callfunc('teacher_package.get_teacher_discipline', cx_Oracle.CURSOR, [login])


def get_discipline(disc_name):
    return cursor.callfunc('discipline_package.get_discipline', cx_Oracle.CURSOR, [disc_name])


def new_discipline(dscpln_name):
    return cursor.callproc('discipline_package.add_discipline', [dscpln_name])


def all_discipline():
    return cursor.callfunc('discipline_package.all_discipline', cx_Oracle.CURSOR, [])


def get_discipline_marks(disc_name):
    return cursor.callfunc('discipline_package.get_discipline_marks', cx_Oracle.CURSOR, [disc_name])


def get_discipline_hw(disc_name):
    return cursor.callfunc('discipline_package.get_discipline_hw', cx_Oracle.CURSOR, [disc_name])


def register_student(login, id):
    return cursor.callfunc('user_package.register_student', cx_Oracle.NUMBER, [login, id])


def register_teacher(login, id):
    return cursor.callfunc('user_package.register_teacher', cx_Oracle.NUMBER, [login, id])


def add_teacher(login, password, id, name):
    return cursor.callproc('teacher_package.add_teacher', [login, password, id, name])


def add_student(login, password, id, name, st_semester):
    return cursor.callproc('student_package.add_student', [login, password, id, name, st_semester])


def delete_student(login):
    return cursor.callproc('student_package.delete_student', [login])


def delete_teacher(login):
    return cursor.callproc('teacher_package.delete_teacher', [login])


def upd_st_password(login, password):
    return cursor.callproc('student_package.update_student_password', [login, password])


def upd_t_password(login, password):
    return cursor.callproc('teacher_package.update_teacher_password', [login, password])
