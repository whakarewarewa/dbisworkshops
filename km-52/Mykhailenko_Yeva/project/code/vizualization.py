import cx_Oracle


class graph1:

    def discipline_count(self):
        ip = '127.0.0.1'
        port = 1521
        SID = 'XE'
        dns_tns = cx_Oracle.makedsn(ip, port, SID)
        connection = cx_Oracle.connect('eve', 'eve', dns_tns)
        cursor = connection.cursor()
        query = 'SELECT  DISCIPLINE_NAME, AVG(MARK) FROM MARK GROUP BY DISCIPLINE_NAME'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
