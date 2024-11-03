def eliminarRegistre(conn):

    cooltra_id = input("Introdueix la id de la cooltra que vols borrar: ")
    cur = conn.cursor()

    sql = '''
        DELETE FROM COOLTRAS
        WHERE cooltra_id = %s;
    '''

    try:

        cur.execute(sql, (cooltra_id))
        conn.commit()

        if cur.rowcount > 0:
            print(f"La cooltra amb l'id: {cooltra_id} s'ha borrat correctament.")
        else:
            print(f"No s'ha trobat cap cooltra amb aquesta id: {cooltra_id}.")

    finally:
        if cur:
            cur.close()
