import pg8000

def logic(v):
    sql = "INSERT INTO value_table (value) VALUES (%s) RETURNING id"
    conn = None
    try:
        conn = pg8000.connect(
            host="localhost",
            database="mcep",
            user="mcep",
            password="mcep"
        )
        cur = conn.cursor()
        cur.execute(sql, (v["x"],))
        value_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return {"z": value_id}
    except Exception as error:
        return {"error": str(error)}
    finally:
        if conn is not None:
            conn.close()
