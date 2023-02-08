import sqlite3 as sq
with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("""SELECT name, old, score, games.data as score
    FROM games
    JOIN users ON games.user_id = users.rowid
    GROUP BY user_id""")

    for i in cur:
        print(i)