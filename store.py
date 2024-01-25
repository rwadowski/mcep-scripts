import psycopg2


def logic(v):
    sql = """INSERT INTO value_table VALUES (%s) RETURNING id"""
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="mcep",
            user="mcep",
            password="mcep"
        )
        cur = conn.cursor()
        cur.execute(sql, v["x"])
        value_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        r = {
            "z": value_id
        }
        return r
    except (Exception, psycopg2.DatabaseError) as error:
        r = {
            "error": str(error)
        }
        return r
    finally:
        if conn is not None:
            conn.close()
