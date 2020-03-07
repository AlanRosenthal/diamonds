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
        price text,
        carat text,
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


def query_db():
    con = db_connect()
    cur = con.cursor()

    cur.execute(
        """
    SELECT * FROM brilliant_earth"""
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    con.commit()
    con.close()


def db_connect():
    con = sqlite3.connect(DB_PATH)
    return con
