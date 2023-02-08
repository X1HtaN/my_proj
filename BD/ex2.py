import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE score > 3000 ORDER BY score DESC LIMIT 5")

    for res in cur:
        print(res)