def crearTaula(conn):

    cur = conn.cursor()

    sql = '''
    CREATE TABLE IF NOT EXISTS COOLTRAS(
        cooltra_id SERIAL PRIMARY KEY,
        cooltra_name VARCHAR(255),
        cooltra_surname VARCHAR(255) NOT NULL,
        cooltra_age BIGINT NOT NULL,
        cooltra_email VARCHAR(255) NOT NULL
    );
    '''

    try:

        cur.execute(sql)
        conn.commit()
        print("La taula COOLTRAS s'ha create correctament.")


    finally:
        if cur:
            cur.close()