def afegirATaula(conn):

    cooltra_name = input("Introdueix nom: ")
    cooltra_surname = input("Introdueix cognom: ")
    cooltra_age = int(input("Introdueix edat: "))
    cooltra_email = input("Introdueix email: ")
    cur = conn.cursor()

    sql = '''
        INSERT INTO COOLTRAS (cooltra_name, cooltra_surname, cooltra_age, cooltra_email)
        VALUES (%s, %s, %s, %s);
    '''
    values = (cooltra_name, cooltra_surname, cooltra_age, cooltra_email)

    try:

        cur.execute(sql, values)
        conn.commit()
        print("S'ha insertat la nova cooltra a COOLTRAS")


    finally:
        if cur:
            cur.close()
