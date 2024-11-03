def actualitzarRegistre(conn):

    cooltra_id = input("Introdueix la id de la cooltra que vols que es modifiqui: ")
    cur = conn.cursor()

    select_sql = '''
        SELECT * FROM COOLTRAS WHERE cooltra_id = %s;
    '''
    cur.execute(select_sql, (cooltra_id,))
    record = cur.fetchone()

    if not record:
        print(f"No s'han trobat cooltras amb l'id: {cooltra_id}.")
        cur.close()
        return None

    print("Dades actuals:")
    print(f"ID: {record[0]}, NOM: {record[1]}, COGNOM: {record[2]}, ANYS: {record[3]}, EMAIL: {record[4]}")

    cooltra_name = input("Introdueix el nou nom :")
    cooltra_surname = input("Introdueix el nou cognom:") or record[2]
    cooltra_age = int(input("Introdueix la nova edat:"))
    cooltra_email = input("Introdueix el nou correu:")

    update_sql = '''
        UPDATE COOLTRAS
        SET cooltra_name = %s, cooltra_surname = %s, cooltra_age = %s, cooltra_email = %s
        WHERE cooltra_id = %s;
    '''
    values = (cooltra_name, cooltra_surname, cooltra_age, cooltra_email, cooltra_id)

    try:
        cur.execute(update_sql, values)
        conn.commit()
        print(f"S'han fet els canvis a la cooltra amb l'id: {cooltra_id}")


    finally:
        if cur:
            cur.close()

