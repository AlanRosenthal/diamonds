import sqlite3

DB_PATH = "store.db"


def create_table(cur):
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

def insert_unique_data(upc, shape, price, carat, clarity, cut, color):
    con = db_connect()
    cur = con.cursor()

    create_table(cur)

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

    create_table(cur)

    cur.execute(
        """
    SELECT * FROM brilliant_earth"""
    )

    rows = cur.fetchall()

    con.commit()
    con.close()

    return len(rows)


def query_db(carat_min, carat_max, shape, color, clarity, cut, price_min, price_max):
    con = db_connect()
    cur = con.cursor()

    color_sql = ",".join([f'"{c}"' for c in color])
    clarity_sql = ",".join([f'"{c}"' for c in clarity])
    cut_sql = ",".join([f'"{c}"' for c in cut])

    create_table(cur)

    cur.execute(
        f"""
    SELECT * FROM brilliant_earth
    WHERE
        carat >= {carat_min} and
        carat <= {carat_max} and
        shape = \"{shape}\" and
        color in ({color_sql}) and
        clarity in ({clarity_sql}) and
        cut in ({cut_sql}) and
        price >= {price_min} and
        price <= {price_max}
    ORDER BY price asc
    """
    )

    rows = cur.fetchall()

    con.commit()
    con.close()

    return rows


def db_connect(db_file=DB_PATH):
    return sqlite3.connect(db_file)
