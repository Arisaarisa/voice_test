import sqlite3


def init_db():
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    with open("schema.sql") as f:
        sql = f.read()

        cursor.executescript(sql)

        conn.commit()

        conn.close()


def find_all_answers():
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM answers"

    answers = cursor.execute(sql).fetchall()

    conn.commit()
    conn.close()

    return answers


def add_answer(this_year, season, after_today):
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    sql = "INSERT INTO answers(thisyear,season,tomorrow) VALUES(?,?,?)"
    cursor.execute(sql, (this_year, season, after_today))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
