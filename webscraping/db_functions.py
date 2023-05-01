import connect as con


""" def db_commit(sql):
    for command in sql:
        con.cursor.execute(command)
        con.db.commit() """


def db_commit(sql, table=""):
    try:
        for command in sql:
            con.cursor.execute(command)
    except Exception:
        sql = f"DROP TABLE {table}"
        con.cursor.execute(sql)
    con.db.commit()


def insert_db(table, year, contest, numbers, date="00/00/0000"):
    n1, n2, n3, n4, n5, n6 = numbers
    sql = [
        f"INSERT INTO {table} (megaYear, contest, n1, n2, n3, n4, n5, n6, dateMega) VALUES ({year}, {contest}, {n1}, {n2}, {n3}, {n4}, {n5}, {n6}, '{date}')"
    ]
    db_commit(sql)


def read_game_db(table):
    con.cursor.execute(f'SELECT * from {table}')
    result = con.cursor.fetchall()
    return result


def create_table(year):
    table = f"mega{year}"
    sql = [
        f"""
        CREATE TABLE {table} (
        megaYear INT,
        contest INT,
        n1 VARCHAR(2),
        n2 VARCHAR(2),
        n3 VARCHAR(2),
        n4 VARCHAR(2),
        n5 VARCHAR(2),
        n6 VARCHAR(2),
        dateMega VARCHAR(30),
        PRIMARY KEY (contest)
        );
        """
    ]

    db_commit(sql, table)
