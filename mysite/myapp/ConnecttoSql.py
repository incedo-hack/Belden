import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_Plugins(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM myapp_plugins")

    rows = cur.fetchall()

    things = []
    for row in rows:
        things.append(dict([('ID',row[0]),
                            ('Product',row[1]),
                            ('BugID', row[2]),
                            ('RuleString', row[3]),
                            ('RCA',row[4])
                            ]))
    return things


def fetchAllPLuginRows(path):
    con = create_connection(path)
    return select_all_Plugins(con)



#if __name__ == "__main__":
#    """conn = create_connection(r"C:\Builds\mysite\db.sqlite3")"""
#    conn = create_connection(r"E:\db.sqlite3")
#
#    select_all_Plugins(conn);
