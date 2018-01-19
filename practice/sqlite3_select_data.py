import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return Connection object or None"""

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_data(conn, select_sql):
    """
    Execute the select_sql statement to get all rows from database
    :param conn: the Connection object
    :param select_sql: the SELECT statement
    :return:
    """
    cur = conn.cursor()
    cur.execute(select_sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = "C:\\Users\\user\\Desktop\\Bella\\sqlite\\db\\chinook.db"

    select_all_customers = "SELECT * FROM customers"

    # create a database connection
    conn = create_connection(database)

    with conn:
        print("Query all customers")
        select_all_data(conn, select_all_customers)


if __name__ == '__main__':
    main()