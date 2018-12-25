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


def get_role(username):
    return cursor.callfunc('user_package.get_role', cx_Oracle.STRING, [username])
