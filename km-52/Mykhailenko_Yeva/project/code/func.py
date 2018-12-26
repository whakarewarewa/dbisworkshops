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


def find_student(sid):
    return cursor.callfunc('student_package.find_student', cx_Oracle.NUMBER, [sid])


def register_teacher(login, id):
    return cursor.callfunc('user_package.register_teacher', cx_Oracle.NUMBER, [login, id])


def find_teacher(tid):
    return cursor.callfunc('teacher_package.find_teacher', cx_Oracle.NUMBER, [tid])


def find_homework(disc_name, tid, hw_date):
    return cursor.callfunc('homework_package.find_homework', cx_Oracle.NUMBER, [disc_name, tid, hw_date])


def find_mark(sid, disc_name, st_year):
    return cursor.callfunc('mark_package.find_mark', cx_Oracle.NUMBER, [sid, disc_name, st_year])


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


def tname_to_id(name):
    return cursor.callfunc('homework_package.tname_to_id', cx_Oracle.STRING, [name])


def login_to_tname(name):
    return cursor.callfunc('teacher_package.login_to_tname', cx_Oracle.STRING, [name])


def sname_to_id(name):
    return cursor.callfunc('mark_package.sname_to_id', cx_Oracle.STRING, [name])


def add_homework(discipline_name, teacher_id, hw_date, hw_description):
    return cursor.callproc('homework_package.add_homework', [discipline_name, teacher_id, hw_date, hw_description])


def delete_homework(discipline_name, teacher_id, hw_date):
    return cursor.callproc('homework_package.delete_homework', [discipline_name, teacher_id, hw_date])


def delete_mark(student_id, discipline_name, st_year):
    return cursor.callproc('mark_package.delete_mark', [student_id, discipline_name, st_year])


def add_mark(student_id, discipline_name, st_year, mark):
    return cursor.callproc('mark_package.add_mark', [student_id, discipline_name, st_year, mark])


