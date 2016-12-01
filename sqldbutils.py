import utils as imutil
import pyodbc

#SQL db setting
dsn = 'sqlserverdatasource'
user = ''
password = ''
database = 'SQLCRIS'


def get_db_connection():
    con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
    cnxn = pyodbc.connect(con_string)
    cursor = cnxn.cursor()
    return {'cnxn': cnxn, 'cursor': cursor}


def release_db_connection(cnn_obj):
    cnn_obj['cnxn'].close()
    cnn_obj['cursor'].close()
    cnn_obj['cnxn'].disconnect()


def query_data(query, read_data_func, container):
    conn_dic = get_db_connection()
    conn_dic['cursor'].execute(query)
    rows = conn_dic['cursor'].fetchall()
    read_data_func(rows, container)
    release_db_connection(conn_dic)
