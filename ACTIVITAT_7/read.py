import psycopg2
from connection import getConnection
def llegirRegistres(conn):

    cur = conn.cursor()

    sql = '''
        SELECT * FROM COOLTRAS;
    '''

    try:

        cur.execute(sql)
        records = cur.fetchall()

        if records:
            print("Registres a la taula COOLTRAS:")
            for record in records:
                print(f"ID: {record[0]}, NOM: {record[1]}, COGNOM: {record[2]}, EDAT: {record[3]}, EMAIL: {record[4]}")
        else:
            print("No records found in COOLTRAS.")

    finally:
        if cur:
            cur.close()


