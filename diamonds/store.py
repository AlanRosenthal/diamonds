import sqlite3

DB_PATH = "store.db"


def insert_unique_data(upc, shape, price, carat, clarity, cut, color):
    con = db_connect()
    cur = con.cursor()

    # Create table if it doesnt
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS brilliant_earth (
        upc text PRIMARY KEY,
        shape text,
        price double,
        carat double,
        clarity text,
        cut text,
        color text)"""
    )

    cur.execute(
        f"""
    INSERT OR IGNORE INTO brilliant_earth VALUES ("{upc}", "{shape}", "{price}", "{carat}", "{clarity}", "{cut}", "{color}")
    """
    )

    con.commit()
    con.close()


def count_entries():
    con = db_connect()
    cur = con.cursor()

    cur.execute(
        """
    SELECT * FROM brilliant_earth"""
    )

    rows = cur.fetchall()

    con.commit()
    con.close()

    return len(rows)


def query_db(carat_min, carat_max, shape, color, clarity, cut):
    con = db_connect()
    cur = con.cursor()

    color_sql = ",".join([f'"{c}"' for c in color])
    clarity_sql = ",".join([f'"{c}"' for c in clarity])
    cut_sql = ",".join([f'"{c}"' for c in cut])

    cur.execute(
        f"""
    SELECT * FROM brilliant_earth
    WHERE
        carat >= {carat_min} and
        carat <= {carat_max} and
        shape = \"{shape}\" and
        color in ({color_sql}) and
        clarity in ({clarity_sql}) and
        cut in ({cut_sql})
    ORDER BY price asc
    """
    )

    rows = cur.fetchall()

    con.commit()
    con.close()

    return rows


def db_connect(db_file=DB_PATH):
    return sqlite3.connect(db_file)
